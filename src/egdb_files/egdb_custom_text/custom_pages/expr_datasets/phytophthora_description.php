<div class="card">
    <h4><i class="fas fa-dna"></i> Phytophthora infestans RNA-seq Expression Atlas</h4>
    <p class="text-justify">
        <strong>Project:</strong> <a href="https://www.ncbi.nlm.nih.gov/bioproject/PRJNA819263" target="_blank">PRJNA819263</a><br>
        <strong>Organism:</strong> <em>Phytophthora infestans</em><br>
        <strong>Experiment:</strong> Comparative RNA-seq analysis of infection stages (2dpi vs 3dpi)<br>
        <strong>Technology:</strong> Illumina RNA sequencing
    </p>
    
    <h5><i class="fas fa-flask"></i> Experimental Design</h5>
    <p class="text-justify">
        This dataset represents a comprehensive RNA-seq analysis of <em>Phytophthora infestans</em> during potato infection. 
        The study compares gene expression profiles at two critical infection timepoints:
        <ul>
            <li><strong>2 dpi:</strong> Early infection stage (2 days post-infection)</li>
            <li><strong>3 dpi:</strong> Established infection stage (3 days post-infection)</li>
        </ul>
        Each condition includes 2 biological replicates, providing robust statistical power for differential expression analysis.
    </p>
    
    <h5><i class="fas fa-chart-bar"></i> Dataset Statistics</h5>
    <div class="row">
        <div class="col-md-6">
            <ul>
                <li><strong>Total genes:</strong> 14,458</li>
                <li><strong>Samples:</strong> 4 (2 conditions × 2 replicates)</li>
                <li><strong>Genes expressed at 2dpi:</strong> 12,183 (84.3%)</li>
                <li><strong>Genes expressed at 3dpi:</strong> 14,458 (100%)</li>
            </ul>
        </div>
        <div class="col-md-6">
            <ul>
                <li><strong>Upregulated in 3dpi:</strong> 3,310 genes (22.9%)</li>
                <li><strong>Downregulated in 3dpi:</strong> 5,136 genes (35.5%)</li>
                <li><strong>Expression values:</strong> RPKM normalized</li>
                <li><strong>Total dataset size:</strong> ~6.7 MB</li>
            </ul>
        </div>
    </div>
    
    <h5><i class="fas fa-cogs"></i> Data Processing Pipeline</h5>
    <p class="text-justify">
        Raw sequencing data was processed using a standardized RNA-seq pipeline:
        <ol>
            <li><strong>Quality Control:</strong> Cutadapt 5.1 for adapter trimming and quality filtering</li>
            <li><strong>Alignment:</strong> HISAT2 2.2.1 for spliced alignment to reference genome</li>
            <li><strong>Quantification:</strong> featureCounts for gene-level read counting</li>
            <li><strong>Normalization:</strong> RPKM (Reads Per Kilobase Million) normalization accounting for gene length and sequencing depth</li>
        </ol>
    </p>
    
    <h5><i class="fas fa-info-circle"></i> Usage Notes</h5>
    <p class="text-justify">
        This expression atlas enables researchers to:
        <ul>
            <li>Identify stage-specific gene expression patterns during infection</li>
            <li>Discover potential virulence factors upregulated during infection progression</li>
            <li>Compare expression profiles with other <em>Phytophthora</em> species</li>
            <li>Integrate expression data with genomic annotations and functional predictions</li>
        </ul>
    </p>
    
    <h5><i class="fas fa-external-link-alt"></i> External Resources</h5>
    <p class="text-justify">
        <a href="https://www.ncbi.nlm.nih.gov/bioproject/PRJNA819263" target="_blank" class="btn btn-primary btn-sm">
            <i class="fas fa-database"></i> View NCBI BioProject
        </a>
        <a href="https://www.ncbi.nlm.nih.gov/sra?term=PRJNA819263" target="_blank" class="btn btn-secondary btn-sm">
            <i class="fas fa-download"></i> Download Raw Data
        </a>
    </p>
</div>
