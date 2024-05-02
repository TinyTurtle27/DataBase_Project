<?php

$dsn = "mysql:host=localhost;dbname=student_registration";
$dbusername = "root";
$dbpassword = "Keter27#88M!";

try { 
    $pdo = new PDO($dsn, $dbusername, $dbpassword);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    echo "Failed: ". $e->getMessage();
}