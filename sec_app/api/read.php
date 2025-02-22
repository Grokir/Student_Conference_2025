<h2> 
  <?php
    if (isset($_GET['file'])) {
      $file_name    = $_GET['file'];
      $workdir_path = '/var/www/php-app/api/';
      $location     = $workdir_path.basename(realpath($file_name));
      echo file_get_contents($location);
    }
  ?>
</h2>
