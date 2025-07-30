#!/usr/bin/env python3
"""
Comprehensive GFF3 annotation extractor for Phytophthora infestans
Creates detailed annotation tables with multiple information types
"""

import re
import sys
from collections import defaultdict

def parse_gff3_attributes(attr_string):
    """Parse GFF3 attributes string into a dictionary"""
    attributes = {}
    for attr in attr_string.split(';'):
        if '=' in attr:
            key, value = attr.split('=', 1)
            # URL decode and clean up values
            value = value.replace('%2C', ',').replace('%3B', ';')
            attributes[key] = value
    return attributes

def extract_comprehensive_annotations(gff_file):
    """Extract comprehensive gene annotations from GFF3 file"""
    
    genes = {}
    gene_children = defaultdict(list)
    
    with open(gff_file, 'r') as f:
        for line in f:
            line = line.strip()
            
            # Skip comments and empty lines
            if line.startswith('#') or not line:
                continue
                
            parts = line.split('\t')
            if len(parts) != 9:
                continue
                
            seqid, source, feature_type, start, end, score, strand, phase, attributes = parts
            attr_dict = parse_gff3_attributes(attributes)
            
            # Process genes
            if feature_type == 'gene':
                gene_id = attr_dict.get('locus_tag') or attr_dict.get('ID') or attr_dict.get('Name')
                if gene_id:
                    genes[gene_id] = {
                        'id': gene_id,
                        'name': attr_dict.get('Name', gene_id),
                        'product': attr_dict.get('product', 'Unknown'),
                        'note': attr_dict.get('Note', ''),
                        'gene_biotype': attr_dict.get('gene_biotype', ''),
                        'dbxref': attr_dict.get('Dbxref', ''),
                        'location': f"{seqid}:{start}-{end}",
                        'strand': strand,
                        'type': feature_type
                    }
            
            # Process child features
            elif feature_type in ['mRNA', 'rRNA', 'tRNA', 'CDS', 'transcript']:
                parent_id = attr_dict.get('Parent')
                if parent_id:
                    parent_id = parent_id.replace('gene-', '')
                    
                    child_info = {
                        'type': feature_type,
                        'product': attr_dict.get('product', ''),
                        'note': attr_dict.get('Note', ''),
                        'name': attr_dict.get('Name', ''),
                        'locus_tag': attr_dict.get('locus_tag', ''),
                        'transcript_id': attr_dict.get('transcript_id', ''),
                        'dbxref': attr_dict.get('Dbxref', '')
                    }
                    gene_children[parent_id].append(child_info)
    
    # Update gene annotations with child feature information
    for gene_id, children in gene_children.items():
        if gene_id in genes:
            best_product = "Unknown"
            best_note = ""
            dbxrefs = set()
            
            for child in children:
                # Priority: CDS > mRNA > rRNA > tRNA > other
                if child['product'] and child['product'] != "Unknown":
                    if child['type'] == 'CDS':
                        best_product = child['product']
                        break
                    elif child['type'] == 'mRNA' and best_product == "Unknown":
                        best_product = child['product']
                    elif child['type'] in ['rRNA', 'tRNA'] and best_product == "Unknown":
                        best_product = child['product']
                        
                if child['note'] and not best_note:
                    best_note = child['note']
                    
                if child['dbxref']:
                    dbxrefs.add(child['dbxref'])
            
            # Update gene annotation
            if best_product != "Unknown":
                genes[gene_id]['product'] = best_product
            if best_note and not genes[gene_id]['note']:
                genes[gene_id]['note'] = best_note
            if dbxrefs and not genes[gene_id]['dbxref']:
                genes[gene_id]['dbxref'] = ','.join(dbxrefs)
    
    return genes

def write_comprehensive_tsv(genes, output_file):
    """Write comprehensive gene annotations to TSV file"""
    
    with open(output_file, 'w') as f:
        # Write header
        f.write("GeneID\tProduct\tNote\tGene_Biotype\tLocation\tStrand\tDbxref\n")
        
        for gene_id in sorted(genes.keys()):
            gene = genes[gene_id]
            
            # Clean up fields
            product = gene['product'] if gene['product'] != 'Unknown' else 'Unknown'
            note = gene['note'].replace('\t', ' ').replace('\n', ' ') if gene['note'] else ''
            biotype = gene['gene_biotype'] if gene['gene_biotype'] else ''
            location = gene['location']
            strand = gene['strand']
            dbxref = gene['dbxref'] if gene['dbxref'] else ''
            
            f.write(f"{gene_id}\t{product}\t{note}\t{biotype}\t{location}\t{strand}\t{dbxref}\n")

def main():
    """Main function"""
    gff_file = "/Users/sathyajali/Documents/jbrowse_build/easyGDB_docker/src/jbrowse/data/potato_lateblight/potato_lateblight_annotation.gff"
    output_file = "/Users/sathyajali/Documents/jbrowse_build/easyGDB_docker/src/downloads/potato_late_blight/Annotations/phytophthora_infestans_comprehensive.tsv"
    
    print("Extracting comprehensive annotations from GFF3 file...")
    genes = extract_comprehensive_annotations(gff_file)
    
    print(f"Found {len(genes)} genes")
    
    # Statistics
    with_products = sum(1 for g in genes.values() if g['product'] != 'Unknown')
    with_notes = sum(1 for g in genes.values() if g['note'])
    with_biotype = sum(1 for g in genes.values() if g['gene_biotype'])
    
    print(f"Genes with product annotations: {with_products} ({with_products/len(genes)*100:.1f}%)")
    print(f"Genes with notes: {with_notes} ({with_notes/len(genes)*100:.1f}%)")
    print(f"Genes with biotype: {with_biotype} ({with_biotype/len(genes)*100:.1f}%)")
    
    print(f"Writing comprehensive annotations to {output_file}")
    write_comprehensive_tsv(genes, output_file)
    
    print("Done!")

if __name__ == "__main__":
    main()
