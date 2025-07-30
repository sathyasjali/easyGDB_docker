<br>
<img class="float-right" style="z-index:0;height:150px" src="<?php echo $images_path.'/species/'.$sps_img ?>" >
<h1><?php echo $sps_subtitle ?></h1>
<h3 style="color:#666"><i><?php echo $sps_title ?></i></h3>
<a href="/jbrowse/" class="btn btn-info sps-btn" role="button">Genome Browser</a>
<a href="/easy_gdb/tools/blast/blast_input.php" class="btn btn-info sps-btn" role="button">BLAST</a>
<a href="/easy_gdb/tools/fasta_download.php" class="btn btn-info sps-btn" role="button">Sequence Extraction</a>
<a href="/easy_gdb/tools/annot_input_list.php?species=phytophthora" class="btn btn-info sps-btn" role="button">Annotation Extraction</a>
<a href="/easy_gdb/downloads.php" class="btn btn-info sps-btn" role="button">Downloads</a>
<br style="clear:both"/>

<h4 class="p_font18">
  About the Species
</h4>
<ul>
  <li>
    <i>Phytophthora infestans</i> is the causal agent of late blight, one of the most destructive diseases affecting potato and tomato crops worldwide.
    This oomycete pathogen infects foliage and tubers, leading to major agricultural losses. The genome of <i>P. infestans</i> is characterized by its large size and high repeat content, which contributes to its adaptability and pathogenicity.
  </li>

  <li>
    Recent transcriptomic analyses have revealed stage-specific expression patterns during host colonization, highlighting the importance of effector proteins and gene regulation dynamics in infection progression.
    For a comprehensive transcriptome and epigenome study during early infection stages (2 and 3 dpi), see:
    <a href="https://www.biorxiv.org/content/10.1101/2022.02.18.480484v1.full" target="_blank">
      Cooke et al., 2022 (bioRxiv)
    </a>. Associated RNA-seq data is available at
    <a href="https://www.ncbi.nlm.nih.gov/bioproject/PRJNA819263" target="_blank">
      NCBI BioProject PRJNA819263
    </a>.
  </li>
</ul>

<br>

<h3>Documents</h3>

<div class="row" style="width:900px;margin-left:0px">

  <div class="col" style="padding:0px">
    <div class="card">
      <div class="card-body">
        <a href="/downloads/Species species 1/Annotations/gene_annotations.txt"><i class='far fa-file-pdf' style='font-size:30px;color:red'></i> Descriptors</a>
      </div>
    </div>
  </div>
  <div class="col" style="padding:0px">
    <div class="card">
      <div class="card-body">
        <a href="/downloads/Species species 1/Sequences/Species_v1.0_cDNA.fasta"><i class='far fa-file-pdf' style='font-size:30px;color:red'></i> Training and Pruning</a>
      </div>
    </div>
  </div>
  <div class="col" style="padding:0px">
    <div class="card">
      <div class="card-body">
        <a href="/downloads/potato_late_blight/Sequences/Species_v1.0_CDS.fasta"><i class='far fa-file-pdf' style='font-size:30px;color:red'></i> Descriptive Guide</a>
      </div>
    </div>
  </div>
</div>
<br>
