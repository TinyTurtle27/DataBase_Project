<?php
include("trash.php");

Function check_login($conn) {
    $_SESSION[''];
    $id = $_SESSION[''];
    $query = $pdo->query('select * from student');
    $data = $query->fetchAll(PDO::FETCH_NUM);
}