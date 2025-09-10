#!/usr/bin/env python3
"""
Enhanced Trinotate Parser with InterPro Description Mapping
"""

import csv
import sys
import re
import json
import requests
from collections import defaultdict

def fetch_interpro_descriptions(interpro_ids):
    """
    Fetch InterPro descriptions from the InterPro API
    
    Args:
        interpro_ids (list): List of InterPro IDs
        
    Returns:
        dict: Mapping of InterPro ID to description
    """
    descriptions = {}
    
    for ipr_id in interpro_ids:
        try:
            url = f"https://www.ebi.ac.uk/interpro/api/entry/InterPro/{ipr_id}/"
            response = requests.get(url, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                descriptions[ipr_id] = data.get('name', '')
            else:
                descriptions[ipr_id] = ''
                
        except Exception as e:
            print(f"Warning: Could not fetch description for {ipr_id}: {e}")
            descriptions[ipr_id] = ''
    
    return descriptions

def parse_trinotate_enhanced(trinotate_file, output_file):
    """
    Enhanced parser with better handling of all annotation types
    """
    
    print(f"Parsing Trinotate report: {trinotate_file}")
    
    output_data = []
    interpro_ids_all = set()
    
    with open(trinotate_file, 'r') as f:
        reader = csv.DictReader(f, delimiter='\t')
        
        for row in reader:
            if row['#gene_id'].startswith('#'):
                continue
                
            gene_id = row['#gene_id']
            
            # Parse annotations
            annotations = {
                'gene': gene_id,
                'araport11': '',
                'description': '',
                'interpro_ids': [],
                'interpro_desc': '',
                'swissprot_id': '',
                'swissprot_desc': '',
                'trembl_id': '',
                'trembl_desc': ''
            }
            
            # Parse SwissProt
            for col in ['sprot_Top_BLASTX_hit', 'sprot_Top_BLASTP_hit']:
                if row.get(col) and row[col] != '.':
                    parts = row[col].split('^')
                    if len(parts) >= 2:
                        # Extract UniProt ID
                        uniprot_full = parts[1]
                        if '|' in uniprot_full:
                            annotations['swissprot_id'] = uniprot_full.split('|')[1]
                        else:
                            annotations['swissprot_id'] = uniprot_full
                        
                        # Extract description
                        if len(parts) >= 6:
                            annotations['swissprot_desc'] = parts[5].strip()
                        break
            
            # Parse TrEMBL
            for col in ['TrEMBL_Top_BLASTX_hit', 'TrEMBL_Top_BLASTP_hit']:
                if row.get(col) and row[col] != '.':
                    parts = row[col].split('^')
                    if len(parts) >= 2:
                        # Extract UniProt ID
                        uniprot_full = parts[1]
                        if '|' in uniprot_full:
                            annotations['trembl_id'] = uniprot_full.split('|')[1]
                        else:
                            annotations['trembl_id'] = uniprot_full
                        
                        # Extract description
                        if len(parts) >= 6:
                            annotations['trembl_desc'] = parts[5].strip()
                        break
            
            # Parse InterPro from multiple sources
            interpro_sources = ['gene_ontology_PFAM', 'gene_ontology_blast', 'Pfam']
            
            for source in interpro_sources:
                if row.get(source) and row[source] != '.':
                    # Find all InterPro IDs
                    ipr_matches = re.findall(r'IPR\d+', row[source])
                    annotations['interpro_ids'].extend(ipr_matches)
            
            # Remove duplicates and add to global set
            annotations['interpro_ids'] = list(set(annotations['interpro_ids']))
            interpro_ids_all.update(annotations['interpro_ids'])
            
            # Set general description
            if annotations['swissprot_desc']:
                annotations['description'] = annotations['swissprot_desc']
            elif annotations['trembl_desc']:
                annotations['description'] = annotations['trembl_desc']
            else:
                annotations['description'] = 'Uncharacterized protein'
            
            output_data.append(annotations)
    
    # Fetch InterPro descriptions
    print(f"Fetching descriptions for {len(interpro_ids_all)} InterPro domains...")
    interpro_descriptions = fetch_interpro_descriptions(list(interpro_ids_all))
    
    # Write output file
    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f, delimiter='\t')
        
        # Write header
        writer.writerow(['Gene', 'Araport11', 'Description', 'InterPro', 'Description', 'SwissProt', 'Description', 'TrEMBL', 'Description'])
        
        # Write data
        for annotation in output_data:
            # Format InterPro
            interpro_id_str = ';'.join(annotation['interpro_ids']) if annotation['interpro_ids'] else ''
            interpro_desc_str = ';'.join([interpro_descriptions.get(ipr, '') for ipr in annotation['interpro_ids']]) if annotation['interpro_ids'] else ''
            
            row = [
                annotation['gene'],
                annotation['araport11'],
                annotation['description'],
                interpro_id_str,
                interpro_desc_str,
                annotation['swissprot_id'],
                annotation['swissprot_desc'],
                annotation['trembl_id'],
                annotation['trembl_desc']
            ]
            
            writer.writerow(row)
    
    print(f"Output written to: {output_file}")
    print(f"Total genes: {len(output_data)}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python trinotate_to_easygdb_enhanced.py <trinotate_report.tsv> <output.tsv>")
        sys.exit(1)
    
    trinotate_file = sys.argv[1]
    output_file = sys.argv[2]
    
    parse_trinotate_enhanced(trinotate_file, output_file)
