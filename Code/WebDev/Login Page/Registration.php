<?php
    include("DataBase.php");

    session_start();
    $db = new DataBase();
    $db->__construct();
    $conn = $db->dbConnect();
    $result = $db->getRegistration($_SESSION["ID"]);
    ?>

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>DataBase Project</title>
  <link rel="stylesheet" href="registration.css">
</head>


<body>
<h2>Registeration Status</h2>
<div class="table-wrapper">
    <table class="fl-table">
        <thead>
        <tr>
            <th>Title</th>
            <th>Instructor</th>
            <th>Meeting Time(s)</th>
            <th>Status</th>
            <th>Action</th>
        </tr>
        </thead>
        <tbody>
            <tr>
                <?php
                    foreach ($result as $row){
                        ?>
                        <td><?php echo $row["Title"]?></td>
                        <td><?php echo $row["Instructor"]?></td>
                        
                        <td><?php echo $row["Meeting"] ?></td>
                        <td><?php echo "w" ?></td>
                        <td><button>DROP</button></td>
                <?php
                    }
                ?>
            </tr>

       
        <tbody>
    </table>
</div>
</body>
</html>