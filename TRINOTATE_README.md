# Phytophthora infestans Trinotate Annotation Pipeline

This directory contains a complete pipeline for annotating Phytophthora infestans genes using Trinotate and formatting the results for EasyGDB.

## Overview

The pipeline includes:
1. **Trinotate annotation pipeline** - Comprehensive functional annotation
2. **Format converter** - Converts Trinotate output to EasyGDB table format
3. **Web interface** - Interactive annotation search and display
4. **Complete workflow** - End-to-end automation script

## Files

### Pipeline Scripts
- `trinotate_pipeline.sh` - Main Trinotate annotation pipeline
- `trinotate_to_easygdb.py` - Basic Trinotate output converter
- `trinotate_to_easygdb_enhanced.py` - Enhanced converter with InterPro API
- `phytophthora_annotation_workflow.sh` - Complete workflow automation

### Web Interface
- `src/easy_gdb/tools/phytophthora_annotations.php` - Interactive annotation search page
- `src/annotations/phytophthora_infestans/phytophthora_comprehensive_annotations.tsv` - Sample annotation data

### Configuration
- `src/easy_gdb/toolbar.php` - Updated navigation menu
- `src/egdb_files/json_files/tools/annotation_links.json` - External database links

## Prerequisites

### Software Requirements
```bash
# Core tools
- Trinotate (latest version)
- TransDecoder
- BLAST+ (makeblastdb, blastx, blastp)
- HMMER (hmmscan)
- InterProScan
- SignalP
- tmHMM

# Python packages
pip install pandas requests

# Databases
- SwissProt
- TrEMBL  
- Pfam-A.hmm
- InterPro
```

### Database Setup
```bash
# Download and format databases
wget ftp://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/complete/uniprot_sprot.fasta.gz
wget ftp://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/complete/uniprot_trembl.fasta.gz

gunzip *.gz
makeblastdb -in uniprot_sprot.fasta -dbtype prot
makeblastdb -in uniprot_trembl.fasta -dbtype prot

# Download Pfam
wget http://ftp.ebi.ac.uk/pub/databases/Pfam/current_release/Pfam-A.hmm.gz
gunzip Pfam-A.hmm.gz
hmmpress Pfam-A.hmm
```

## Usage

### Quick Start (Automated)
```bash
# Edit configuration in phytophthora_annotation_workflow.sh
# Set paths for your system
./phytophthora_annotation_workflow.sh
```

### Manual Pipeline

#### 1. Prepare Input Data
```bash
# Get Phytophthora infestans transcriptome
wget "http://fungidb.org/common/downloads/release-XX/PinfestansT30-4/fasta/data/FungiDB-XX_PinfestansT30-4_AnnotatedTranscripts.fasta"
```

#### 2. Run Trinotate Pipeline
```bash
# Edit paths in trinotate_pipeline.sh
./trinotate_pipeline.sh
```

#### 3. Convert to EasyGDB Format
```bash
# Basic converter
python3 trinotate_to_easygdb.py trinotate_annotation_report.tsv phytophthora_annotations.tsv

# Enhanced converter (with InterPro descriptions)
python3 trinotate_to_easygdb_enhanced.py trinotate_annotation_report.tsv phytophthora_annotations.tsv
```

#### 4. Install in EasyGDB
```bash
cp phytophthora_annotations.tsv src/annotations/phytophthora_infestans/phytophthora_comprehensive_annotations.tsv
```

#### 5. Start EasyGDB
```bash
docker-compose up -d
```

## Web Interface Usage

1. **Access the tool**: http://localhost:8000/easy_gdb/tools/phytophthora_annotations.php

2. **Search genes**: Enter gene IDs (one per line):
   ```
   PITG_00002
   PITG_00003
   PITG_15001
   ```

3. **Features**:
   - Interactive table with sorting and filtering
   - Column-specific search boxes
   - Direct links to external databases (SwissProt, TrEMBL, InterPro, Araport11)
   - Checkbox selection for batch operations
   - Responsive design for mobile devices

## Output Format

The annotation table contains these columns:

| Column | Description | Example |
|--------|-------------|---------|
| Gene | Gene identifier | PITG_00002 |
| Araport11 | Arabidopsis homolog | AT5G10810.1 |
| Description | Functional description | enhancer of rudimentary protein |
| InterPro | InterPro domain IDs | IPR035912;IPR000781 |
| Description | InterPro descriptions | Enhancer of rudimentary superfamily;Enhancer of rudimentary |
| SwissProt | SwissProt protein ID | Q96319 |
| Description | SwissProt description | Enhancer of rudimentary homolog |
| TrEMBL | TrEMBL protein ID | A9NRX8 |
| Description | TrEMBL description | Enhancer of rudimentary homolog |

## Troubleshooting

### Common Issues

1. **Missing databases**
   ```bash
   # Ensure all databases are downloaded and indexed
   ls -la /path/to/databases/
   ```

2. **InterProScan timeout**
   ```bash
   # Increase timeout in InterProScan
   interproscan.sh -cpu 8 --goterms --iprlookup -t n
   ```

3. **Memory issues**
   ```bash
   # Reduce thread count for large datasets
   # Edit pipeline scripts to use fewer CPU cores
   ```

4. **Web interface not loading**
   ```bash
   # Check Docker container status
   docker-compose ps
   
   # Check file permissions
   chmod 644 src/annotations/phytophthora_infestans/*
   ```

## Customization

### Adding New Annotation Sources
Edit `trinotate_to_easygdb_enhanced.py` to parse additional columns from Trinotate output.

### Modifying Web Interface
Edit `src/easy_gdb/tools/phytophthora_annotations.php` to customize:
- Search functionality
- Table styling
- Export options
- Column visibility

### Database Links
Edit `src/egdb_files/json_files/tools/annotation_links.json` to add/modify external database links.

## Performance Notes

- **Large datasets**: Use cluster computing for >100K sequences
- **Memory usage**: 16GB+ RAM recommended for full pipeline
- **Runtime**: ~24-48 hours for complete Phytophthora genome annotation
- **Web interface**: Optimized for datasets up to 50K genes

## Citation

If you use this pipeline, please cite:
- Trinotate: https://github.com/Trinotate/Trinotate
- EasyGDB: Your EasyGDB publication
- Individual tools as appropriate

## Support

For issues and questions:
1. Check the troubleshooting section
2. Review log files in the working directory
3. Submit issues with log files and system information
