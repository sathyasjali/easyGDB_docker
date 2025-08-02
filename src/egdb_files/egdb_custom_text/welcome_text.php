<div class="container-fluid" style="max-width: 1400px; margin: 0 auto; height: 100vh; overflow: hidden;">
  <!-- Full Height Hero Section with Large Image -->
  <div style="position: relative; width: 100vw; margin-left: calc(-50vw + 50%); height: 400px; overflow: hidden; margin-bottom: 20px;">
    <img src='<?php echo "$images_path/Late_blight_on_potato_leaf_2.jpg";?>' 
         alt='Late blight symptoms on potato leaf caused by Phytophthora infestans' 
         style="width: 100%; height: 100%; object-fit: cover; object-position: center;">
    
    <!-- Enhanced Title Overlay -->
    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); text-align: center; color: white; z-index: 10;">
      <div style="background: rgba(0, 0, 0, 0.8); padding: 25px 40px; border-radius: 12px; backdrop-filter: blur(5px); border: 1px solid rgba(255,255,255,0.2);">
        <h1 style="color: white; font-size: 2.2rem; margin-bottom: 8px; text-shadow: 2px 2px 4px rgba(0,0,0,0.9); font-weight: 700;">
          Welcome to <?php echo "$dbTitle";?>
        </h1>
        <h4 style="color: #f8f9fa; font-style: italic; margin: 0; font-size: 1.3rem; text-shadow: 1px 1px 2px rgba(0,0,0,0.8);">
          Comprehensive genomics portal for <em>Phytophthora infestans</em>
        </h4>
        <div style="margin-top: 12px;">
          <span style="background: rgba(34, 157, 255, 0.9); padding: 8px 20px; border-radius: 20px; font-size: 1rem; font-weight: 500; color: white;">
            Advancing Plant Pathology Research
          </span>
        </div>
      </div>
    </div>
  </div>

  <!-- Compact Content Row -->
  <div class="row" style="margin: 0 15px 10px; height: calc(100vh - 460px);">
    <!-- Left Column: Stats + Description -->
    <div class="col-md-8">
      <!-- Compact Statistics -->
      <div style="background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%); border-radius: 8px; padding: 10px; margin-bottom: 10px;">
        <div class="row text-center">
          <div class="col-3">
            <div style="font-size: 1.6rem; font-weight: bold; color: #229dff;">1</div>
            <div style="font-size: 0.9rem; color: #6c757d;">Genome</div>
          </div>
          <div class="col-3">
            <div style="font-size: 1.6rem; font-weight: bold; color: #28a745;">17,797</div>
            <div style="font-size: 0.9rem; color: #6c757d;">Genes</div>
          </div>
          <div class="col-3">
            <div style="font-size: 1.6rem; font-weight: bold; color: #ffc107;">∞</div>
            <div style="font-size: 0.9rem; color: #6c757d;">Research</div>
          </div>
          <div class="col-3">
            <div style="font-size: 1.6rem; font-weight: bold; color: #dc3545;">24/7</div>
            <div style="font-size: 0.9rem; color: #6c757d;">Access</div>
          </div>
        </div>
      </div>
      
      <!-- Compact Description -->
      <div style="background: white; padding: 12px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); height: calc(100% - 60px); overflow-y: auto;">
        <h4 style="color: #2c3e50; margin-bottom: 10px; font-size: 1.3rem;">
          About Our Database
        </h4>
        <p style="font-size: 14px; line-height: 1.5; text-align: justify; margin-bottom: 10px; color: #495057;">
          Comprehensive genomic resources for <em>Phytophthora infestans</em>, the devastating pathogen causing potato and tomato late blight. 
          Our platform integrates genome sequences, annotations, and analytical tools for plant pathology research.
        </p>
        <p style="font-size: 14px; line-height: 1.5; text-align: justify; margin-bottom: 10px; color: #495057;">
          <em>P. infestans</em> caused the Irish Potato Famine and continues threatening global food security. 
          Understanding its genomic architecture is crucial for developing disease management strategies.
        </p>
        <div style="background: #e3f2fd; padding: 8px; border-radius: 6px; border-left: 3px solid #2196f3;">
          <p style="margin: 0; font-size: 13px; color: #1565c0;">
            <strong>Impact:</strong> Serving researchers worldwide with essential tools for pathogen evolution, 
            host-pathogen interactions, and resistance strategy development.
          </p>
        </div>
      </div>
    </div>
    
    <!-- Right Column: Features & Quick Access -->
    <div class="col-md-4">
      <div style="background: white; padding: 12px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); height: 100%;">
        <h5 style="color: #2c3e50; margin-bottom: 10px; font-size: 1.1rem; border-bottom: 2px solid #229dff; padding-bottom: 4px;">
          <i class="fas fa-star" style="color: #ffc107;"></i> Features & Tools
        </h5>
        
        <div style="margin-bottom: 12px;">
          <ul style="font-size: 13px; line-height: 1.4; color: #495057; padding-left: 15px; margin-bottom: 0;">
            <li style="margin-bottom: 4px;">Interactive genome browser (JBrowse)</li>
            <li style="margin-bottom: 4px;">BLAST sequence analysis tools</li>
            <li style="margin-bottom: 4px;">Gene annotations & protein data</li>
            <li style="margin-bottom: 4px;">Downloadable research datasets</li>
          </ul>
        </div>
        
        <h6 style="color: #2c3e50; margin-bottom: 8px; font-size: 1rem;">
          <i class="fas fa-rocket" style="color: #28a745;"></i> Quick Access
        </h6>
        <div style="display: flex; flex-direction: column; gap: 6px;">
          <a href="/easy_gdb/tools/blast/blast_input.php" class="btn btn-primary btn-sm" style="text-align: left; padding: 8px 12px; font-size: 13px;">
            <i class="fas fa-search" style="margin-right: 6px;"></i> BLAST Search
          </a>
          <a href="/jbrowse/?data=data/potato_lateblight" class="btn btn-outline-primary btn-sm" style="text-align: left; padding: 8px 12px; font-size: 13px;">
            <i class="fas fa-eye" style="margin-right: 6px;"></i> Genome Browser
          </a>
          <a href="/easy_gdb/downloads.php" class="btn btn-outline-secondary btn-sm" style="text-align: left; padding: 8px 12px; font-size: 13px;">
            <i class="fas fa-download" style="margin-right: 6px;"></i> Downloads
          </a>
        </div>
        
        <!-- Citation at bottom -->
        <div style="position: absolute; bottom: 15px; left: 15px; right: 15px;">
          <div style="padding: 8px; background: #f8f9fa; border-radius: 4px; border-left: 3px solid #229dff;">
            <p style="margin: 0; font-size: 12px; color: #6c757d;">
              <i class="fas fa-image" style="margin-right: 3px;"></i>
              <strong>Image:</strong> <a href="https://en.wikipedia.org/wiki/Phytophthora_infestans#/media/File:Late_blight_on_potato_leaf_2.jpg" target="_blank" style="color: #229dff;">Wikipedia</a>
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>

</div>