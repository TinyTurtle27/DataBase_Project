<?php
    include("trash.php");
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>

<?php
        $query = $pdo->query('select * from student');
        $data = $query->fetchAll(PDO::FETCH_NUM);
        echo print_r($data);
?>
    
</body>
</html>