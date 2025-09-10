#!/usr/bin/env python3
"""
Combine basic gene annotations with comprehensive database annotations
into a single file for better user experience.
"""

import csv
import os

def combine_annotation_files():
    base_dir = "/Users/sathyajali/Documents/jbrowse_build/easyGDB_docker/src/annotations/phytophthora_infestans"
    
    basic_file = os.path.join(base_dir, "gene_annotations.tsv")
    comprehensive_file = os.path.join(base_dir, "phytophthora_comprehensive_annotations.tsv")
    output_file = os.path.join(base_dir, "phytophthora_complete_annotations.tsv")
    
    print("Combining annotation files...")
    
    # Read basic annotations into a dictionary
    basic_data = {}
    with open(basic_file, 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter='\t')
        for row in reader:
            gene_id = row['GeneID']
            basic_data[gene_id] = row
    
    # Read comprehensive annotations and combine
    combined_rows = []
    
    with open(comprehensive_file, 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter='\t')
        
        # Create combined header
        basic_headers = ['GeneID', 'Product', 'Note', 'Gene_Biotype', 'Location', 'Strand', 'Dbxref']
        comprehensive_headers = ['Araport11', 'Araport11_Description', 'InterPro', 'InterPro_Description', 
                               'SwissProt', 'SwissProt_Description', 'TrEMBL', 'TrEMBL_Description']
        
        combined_header = basic_headers + comprehensive_headers
        combined_rows.append(combined_header)
        
        for row in reader:
            gene_id = row['Gene']
            
            # Get basic annotation data
            basic_info = basic_data.get(gene_id, {})
            
            # Create combined row
            combined_row = [
                gene_id,  # GeneID
                basic_info.get('Product', ''),
                basic_info.get('Note', ''),
                basic_info.get('Gene_Biotype', ''),
                basic_info.get('Location', ''),
                basic_info.get('Strand', ''),
                basic_info.get('Dbxref', ''),
                row.get('Araport11', ''),  # Araport11
                row.get('Description', ''),  # Araport11_Description (first description)
                row.get('InterPro', ''),
                list(row.values())[4] if len(row.values()) > 4 else '',  # InterPro_Description
                row.get('SwissProt', ''),
                list(row.values())[6] if len(row.values()) > 6 else '',  # SwissProt_Description
                row.get('TrEMBL', ''),
                list(row.values())[8] if len(row.values()) > 8 else ''   # TrEMBL_Description
            ]
            
            combined_rows.append(combined_row)
    
    # Write combined file
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerows(combined_rows)
    
    print(f"Created combined annotation file: {output_file}")
    print(f"Total genes: {len(combined_rows) - 1}")
    
    return output_file

if __name__ == "__main__":
    combine_annotation_files()
