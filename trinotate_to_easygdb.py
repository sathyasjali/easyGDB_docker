#!/usr/bin/env python3
"""
Trinotate to EasyGDB Annotation Formatter
Converts Trinotate annotation report to EasyGDB-compatible annotation table
"""

import pandas as pd
import sys
import re
import argparse

def parse_trinotate_report(trinotate_file, output_file):
    """
    Parse Trinotate annotation report and format for EasyGDB
    
    Args:
        trinotate_file (str): Path to Trinotate annotation report
        output_file (str): Path to output EasyGDB annotation file
    """
    
    print(f"Reading Trinotate report: {trinotate_file}")
    
    # Read Trinotate report
    df = pd.read_csv(trinotate_file, sep='\t', comment='#')
    
    # Initialize output dataframe
    output_data = []
    
    for index, row in df.iterrows():
        gene_id = row['#gene_id']
        transcript_id = row['transcript_id']
        
        # Use gene_id as primary identifier
        if pd.isna(gene_id) or gene_id == '.':
            gene_id = transcript_id
        
        # Extract annotations
        sprot_top_blastx = row['sprot_Top_BLASTX_hit'] if not pd.isna(row['sprot_Top_BLASTX_hit']) and row['sprot_Top_BLASTX_hit'] != '.' else ''
        sprot_top_blastp = row['sprot_Top_BLASTP_hit'] if not pd.isna(row['sprot_Top_BLASTP_hit']) and row['sprot_Top_BLASTP_hit'] != '.' else ''
        trembl_top_blastx = row['TrEMBL_Top_BLASTX_hit'] if not pd.isna(row['TrEMBL_Top_BLASTX_hit']) and row['TrEMBL_Top_BLASTX_hit'] != '.' else ''
        trembl_top_blastp = row['TrEMBL_Top_BLASTP_hit'] if not pd.isna(row['TrEMBL_Top_BLASTP_hit']) and row['TrEMBL_Top_BLASTP_hit'] != '.' else ''
        
        # Parse SwissProt information
        swissprot_id = ''
        swissprot_desc = ''
        if sprot_top_blastx:
            parts = sprot_top_blastx.split('^')
            if len(parts) >= 2:
                swissprot_id = parts[1].split('|')[1] if '|' in parts[1] else parts[1]
                swissprot_desc = parts[5] if len(parts) > 5 else ''
        elif sprot_top_blastp:
            parts = sprot_top_blastp.split('^')
            if len(parts) >= 2:
                swissprot_id = parts[1].split('|')[1] if '|' in parts[1] else parts[1]
                swissprot_desc = parts[5] if len(parts) > 5 else ''
        
        # Parse TrEMBL information
        trembl_id = ''
        trembl_desc = ''
        if trembl_top_blastx:
            parts = trembl_top_blastx.split('^')
            if len(parts) >= 2:
                trembl_id = parts[1].split('|')[1] if '|' in parts[1] else parts[1]
                trembl_desc = parts[5] if len(parts) > 5 else ''
        elif trembl_top_blastp:
            parts = trembl_top_blastp.split('^')
            if len(parts) >= 2:
                trembl_id = parts[1].split('|')[1] if '|' in parts[1] else parts[1]
                trembl_desc = parts[5] if len(parts) > 5 else ''
        
        # Parse Pfam domains
        pfam_domains = row['Pfam'] if not pd.isna(row['Pfam']) and row['Pfam'] != '.' else ''
        
        # Parse InterPro domains and descriptions
        interpro_ids = []
        interpro_descs = []
        
        if not pd.isna(row['gene_ontology_PFAM']) and row['gene_ontology_PFAM'] != '.':
            go_terms = row['gene_ontology_PFAM'].split('`')
            for term in go_terms:
                if 'IPR' in term:
                    # Extract InterPro IDs
                    ipr_matches = re.findall(r'IPR\d+', term)
                    interpro_ids.extend(ipr_matches)
        
        if not pd.isna(row['Pfam']) and row['Pfam'] != '.':
            pfam_entries = row['Pfam'].split('`')
            for entry in pfam_entries:
                if 'IPR' in entry:
                    # Extract InterPro info from Pfam column
                    parts = entry.split('^')
                    for part in parts:
                        if 'IPR' in part:
                            ipr_id = re.search(r'IPR\d+', part)
                            if ipr_id:
                                interpro_ids.append(ipr_id.group())
        
        # Get general description (use best available)
        description = ''
        if swissprot_desc:
            description = swissprot_desc
        elif trembl_desc:
            description = trembl_desc
        elif pfam_domains:
            # Extract description from Pfam
            pfam_parts = pfam_domains.split('^')
            if len(pfam_parts) > 4:
                description = pfam_parts[4]
        
        # Clean up descriptions
        description = re.sub(r'\s+', ' ', description).strip()
        swissprot_desc = re.sub(r'\s+', ' ', swissprot_desc).strip()
        trembl_desc = re.sub(r'\s+', ' ', trembl_desc).strip()
        
        # Format InterPro data
        interpro_id_str = ';'.join(list(set(interpro_ids))) if interpro_ids else ''
        interpro_desc_str = ''  # Would need additional parsing for detailed descriptions
        
        # Find best Araport11 homolog (placeholder - would need actual ortholog mapping)
        araport11_id = ''
        if 'AT' in str(row).upper():
            # Look for Arabidopsis gene IDs in the row
            at_matches = re.findall(r'AT[0-9]G[0-9]+', str(row).upper())
            if at_matches:
                araport11_id = at_matches[0] + '.1'  # Add version number
        
        # Create output row
        output_row = {
            'Gene': gene_id,
            'Araport11': araport11_id,
            'Description': description,
            'InterPro': interpro_id_str,
            'Description.1': interpro_desc_str,
            'SwissProt': swissprot_id,
            'Description.2': swissprot_desc,
            'TrEMBL': trembl_id,
            'Description.3': trembl_desc
        }
        
        output_data.append(output_row)
    
    # Create output DataFrame
    output_df = pd.DataFrame(output_data)
    
    # Remove duplicates based on Gene ID
    output_df = output_df.drop_duplicates(subset=['Gene'])
    
    # Rename columns to match EasyGDB format
    output_df.columns = ['Gene', 'Araport11', 'Description', 'InterPro', 'Description', 'SwissProt', 'Description', 'TrEMBL', 'Description']
    
    # Save to file
    output_df.to_csv(output_file, sep='\t', index=False)
    
    print(f"Formatted annotation table saved to: {output_file}")
    print(f"Total genes processed: {len(output_df)}")
    print(f"Genes with SwissProt hits: {len(output_df[output_df['SwissProt'] != ''])}")
    print(f"Genes with TrEMBL hits: {len(output_df[output_df['TrEMBL'] != ''])}")
    print(f"Genes with InterPro domains: {len(output_df[output_df['InterPro'] != ''])}")

def main():
    parser = argparse.ArgumentParser(description='Convert Trinotate report to EasyGDB annotation format')
    parser.add_argument('trinotate_file', help='Input Trinotate annotation report file')
    parser.add_argument('output_file', help='Output EasyGDB annotation file')
    parser.add_argument('--species', default='phytophthora_infestans', help='Species name')
    
    args = parser.parse_args()
    
    try:
        parse_trinotate_report(args.trinotate_file, args.output_file)
        print("Conversion completed successfully!")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
