<div class="container-fluid" style="max-width: 1400px; margin: 0 auto;">
  <!-- Hero Section with Full-Width Image -->
  <div style="position: relative; width: 100vw; margin-left: calc(-50vw + 50%); height: 250px; overflow: hidden; margin-bottom: 25px;">
    <img src='<?php echo "$images_path/Late_blight_on_potato_leaf_2.jpg";?>' 
         alt='Late blight symptoms on potato leaf caused by Phytophthora infestans' 
         style="width: 100%; height: 100%; object-fit: cover; object-position: center;">
    
    <!-- Centered Title Overlay -->
    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); text-align: center; color: white; z-index: 10;">
      <div style="background: rgba(0, 0, 0, 0.6); padding: 20px 30px; border-radius: 8px; backdrop-filter: blur(3px);">
        <h1 style="color: white; font-size: 2.2rem; margin-bottom: 8px; text-shadow: 2px 2px 4px rgba(0,0,0,0.7);">
          Welcome to <?php echo "$dbTitle";?>
        </h1>
        <h4 style="color: #f0f0f0; font-style: italic; margin: 0; font-size: 1.1rem; text-shadow: 1px 1px 2px rgba(0,0,0,0.7);">
          A genomics portal dedicated to <em>Phytophthora infestans</em>
        </h4>
      </div>
    </div>
  </div>

  <!-- Content Section with wider layout -->
  <div class="row" style="margin: 0 25px 10px;">
    <div class="col-xs-12 col-sm-12 col-md-12 col-lg-12">
      <div class="row">
        <div class="col-md-7 col-lg-8">
          <p style="font-size: 16px; line-height: 1.5; text-align: justify; margin-bottom: 15px;">
            This database provides comprehensive genomic resources for <em>Phytophthora infestans</em>, 
            the devastating oomycete pathogen responsible for potato and tomato late blight disease. 
            Our platform integrates genome sequences, gene annotations, protein data, and analytical 
            tools to support research in plant pathology, disease resistance, and crop protection.
          </p>
          
          <p style="font-size: 16px; line-height: 1.5; text-align: justify; margin-bottom: 15px;">
            <em>Phytophthora infestans</em> caused the Irish Potato Famine and continues to threaten 
            global food security. Understanding its genomic architecture and gene expression patterns 
            is crucial for developing effective disease management strategies.
          </p>
        </div>
        
        <div class="col-md-5 col-lg-4">
          <div style="margin-top: 0;">
            <h5><strong>Key Features:</strong></h5>
            <ul style="font-size: 14px; line-height: 1.4; margin-bottom: 15px;">
              <li>Comprehensive genome browser with JBrowse visualization</li>
              <li>BLAST search tools for sequence similarity analysis</li>
              <li>Gene annotations and functional classifications</li>
              <li>Protein sequences and domain analysis</li>
              <li>Downloadable datasets for research use</li>
            </ul>
            
            <div>
              <h5><strong>Quick Access:</strong></h5>
              <div style="margin-top: 10px;">
                <a href="/easy_gdb/tools/blast/blast_input.php" class="btn btn-primary btn-sm" style="margin-bottom: 5px; margin-right: 5px;">
                  <i class="fas fa-search"></i> BLAST Search
                </a>
                <a href="/easy_gdb/downloads.php" class="btn btn-outline-primary btn-sm" style="margin-bottom: 5px; margin-right: 5px;">
                  <i class="fas fa-download"></i> Downloads
                </a>
                <a href="/easy_gdb/tools/jbrowse/" class="btn btn-outline-secondary btn-sm" style="margin-bottom: 5px;">
                  <i class="fas fa-eye"></i> Genome Browser
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  
  <!-- Citation Section -->
  <div style="margin: 5px 15px 0; padding: 6px; background-color: #f8f9fa; border-left: 4px solid #229dff; border-radius: 4px;">
    <p style="margin: 0; font-size: 12px; color: #666;">
      <strong>Image Source:</strong> Late blight on potato leaf. 
      <a href="https://en.wikipedia.org/wiki/Phytophthora_infestans#/media/File:Late_blight_on_potato_leaf_2.jpg" 
         target="_blank" style="color: #229dff;">
        Wikipedia - Phytophthora infestans
      </a>
    </p>
  </div>

</div>