#!/usr/bin/env python3
"""
Enhanced GFF3 annotation extractor for Phytophthora infestans
Extracts gene annotations with proper product information from child features
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

def extract_annotations_from_gff3(gff_file):
    """Extract gene annotations from GFF3 file with improved product detection"""
    
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
                        'type': feature_type
                    }
            
            # Process child features (mRNA, rRNA, tRNA, CDS, etc.)
            elif feature_type in ['mRNA', 'rRNA', 'tRNA', 'CDS', 'transcript']:
                parent_id = attr_dict.get('Parent')
                if parent_id:
                    # Clean parent ID (remove prefix if present)
                    parent_id = parent_id.replace('gene-', '')
                    
                    child_info = {
                        'type': feature_type,
                        'product': attr_dict.get('product', ''),
                        'note': attr_dict.get('Note', ''),
                        'name': attr_dict.get('Name', ''),
                        'locus_tag': attr_dict.get('locus_tag', ''),
                        'transcript_id': attr_dict.get('transcript_id', '')
                    }
                    gene_children[parent_id].append(child_info)
    
    # Update gene annotations with child feature information
    for gene_id, children in gene_children.items():
        if gene_id in genes:
            # Look for product information in children
            best_product = "Unknown"
            best_note = ""
            
            for child in children:
                # Priority order: CDS > mRNA > rRNA > tRNA > other
                if child['product'] and child['product'] != "Unknown":
                    if child['type'] == 'CDS':
                        best_product = child['product']
                        break  # CDS product is highest priority
                    elif child['type'] == 'mRNA' and best_product == "Unknown":
                        best_product = child['product']
                    elif child['type'] in ['rRNA', 'tRNA'] and best_product == "Unknown":
                        best_product = child['product']
                        
                # Also collect notes
                if child['note'] and not best_note:
                    best_note = child['note']
            
            # Update gene annotation if we found better information
            if best_product != "Unknown":
                genes[gene_id]['product'] = best_product
            if best_note and not genes[gene_id]['note']:
                genes[gene_id]['note'] = best_note
    
    return genes

def write_annotation_tsv(genes, output_file):
    """Write gene annotations to TSV file"""
    
    with open(output_file, 'w') as f:
        # Write header
        f.write("GeneID\tProduct\n")
        
        # Write gene annotations sorted by gene ID
        for gene_id in sorted(genes.keys()):
            gene = genes[gene_id]
            product = gene['product']
            
            # Clean up product description
            if product and product != "Unknown":
                # Remove redundant phrases and clean up
                product = product.replace('hypothetical protein', 'Unknown')
                product = product.replace('uncharacterized protein', 'Unknown')
            
            f.write(f"{gene_id}\t{product}\n")

def main():
    """Main function"""
    gff_file = "/Users/sathyajali/Documents/jbrowse_build/easyGDB_docker/src/jbrowse/data/potato_lateblight/potato_lateblight_annotation.gff"
    output_file = "/Users/sathyajali/Documents/jbrowse_build/easyGDB_docker/src/downloads/potato_late_blight/Annotations/phytophthora_infestans_annotations_improved.tsv"
    
    print("Extracting annotations from GFF3 file...")
    genes = extract_annotations_from_gff3(gff_file)
    
    print(f"Found {len(genes)} genes")
    
    # Count how many have proper product annotations
    with_products = sum(1 for g in genes.values() if g['product'] != 'Unknown')
    print(f"Genes with product annotations: {with_products} ({with_products/len(genes)*100:.1f}%)")
    
    print(f"Writing improved annotations to {output_file}")
    write_annotation_tsv(genes, output_file)
    
    print("Done!")
    
    # Show some examples
    print("\nSample annotations:")
    for i, (gene_id, gene) in enumerate(sorted(genes.items())[:10]):
        print(f"  {gene_id}: {gene['product']}")

if __name__ == "__main__":
    main()
