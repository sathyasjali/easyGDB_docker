<?php
// PhytophoraDB Production Configuration
// Phytophthora infestans Genomics Database

$site_config = [
    'site_name' => 'PhytophoraDB',
    'site_subtitle' => 'Phytophthora infestans Genome & Annotation Portal',
    'institution' => 'Your Research Institution',
    'contact_email' => 'contact@phytophoradb.org',
    'version' => '1.0',
    'description' => 'Comprehensive genomics resource for Phytophthora infestans research and late blight disease studies',
    'logo' => 'phytophthora_logo.png',
    'primary_color' => '#2E5D3E', // Forest green for pathogen
    'secondary_color' => '#8B4513', // Brown for disease
    'accent_color' => '#CD853F'     // Sandy brown
];

// Database configuration for production
$production_db = [
    'host' => 'phytophoradb_db',
    'database' => 'phytophoradb_production',
    'username' => 'phytophora_user',
    'password' => getenv('PHYTOPHORADB_DB_PASS'),
    'port' => 5432
];

// Species configuration
$species_list = [
    'Phytophthora_infestans' => [
        'card_title' => 'Phytophthora infestans',
        'card_subtitle' => 'Late Blight Pathogen',
        'image' => 'phytophthora_infestans.png',
        'public' => true,
        'link' => 'phytophthora_infestans.php',
        'genome_size' => '240 Mb',
        'gene_count' => '18,720',
        'assembly_version' => 'Pi_v1.0',
        'description' => 'Causative agent of potato and tomato late blight disease'
    ]
];

// Expression datasets configuration
$expression_datasets = [
    'Phytophthora_infection_timecourse.txt' => [
        'title' => 'Late Blight Infection Time Course',
        'description' => 'Gene expression during potato leaf infection by P. infestans',
        'conditions' => ['0h', '6h', '12h', '24h', '48h', '72h', '96h'],
        'samples' => 21,
        'publication' => 'DOI: 10.1234/phytophthora-timecourse'
    ],
    'Phytophthora_effector_expression.txt' => [
        'title' => 'Effector Protein Expression',
        'description' => 'Expression profiles of RXLR and CRN effector genes',
        'conditions' => ['Mycelium', 'Sporangia', 'Zoospores', 'Infection'],
        'samples' => 16,
        'publication' => 'DOI: 10.1234/effector-expression'
    ],
    'Phytophthora_host_interaction.txt' => [
        'title' => 'Host-Pathogen Interaction',
        'description' => 'Comparative expression during compatible vs incompatible interactions',
        'conditions' => ['Compatible', 'Incompatible', 'R-gene mediated'],
        'samples' => 18,
        'publication' => 'DOI: 10.1234/host-pathogen'
    ]
];

// Tools configuration
$tools_config = [
    'blast' => true,
    'expression' => true,
    'annotations' => true,
    'sequence_extraction' => true,
    'gene_enrichment' => true,
    'jbrowse' => true,
    'variants' => true,
    'effector_prediction' => true,
    'orthology' => true
];

// Phytophthora-specific features
$phytophthora_features = [
    'effector_genes' => [
        'rxlr_effectors' => 563,
        'crn_effectors' => 196,
        'necrosis_effectors' => 85
    ],
    'pathogenicity_factors' => [
        'cell_wall_degrading_enzymes' => 435,
        'proteases' => 124,
        'lipases' => 67
    ],
    'genome_statistics' => [
        'genome_size_mb' => 240,
        'protein_coding_genes' => 18720,
        'repeat_content_percent' => 74.3,
        'gc_content_percent' => 51.2
    ]
];

// Research categories
$research_categories = [
    'Late Blight Disease' => [
        'description' => 'Genes involved in potato and tomato late blight pathogenesis',
        'gene_count' => 2340
    ],
    'Effector Proteins' => [
        'description' => 'RXLR and CRN effector proteins for host manipulation',
        'gene_count' => 759
    ],
    'Spore Formation' => [
        'description' => 'Genes controlling sporangia and zoospore development',
        'gene_count' => 1250
    ],
    'Host Recognition' => [
        'description' => 'Pathogen recognition and host specificity factors',
        'gene_count' => 890
    ],
    'Drug Targets' => [
        'description' => 'Potential targets for fungicide development',
        'gene_count' => 456
    ]
];
?>
