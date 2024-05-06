<?php

$host = "Localhost";
$user="root";
$pass= "yoti123";
$db="student_database";

$conn=mysqli_connect($host, $user, $pass, $db);

if (!$conn) {
    die("Failed to connect to Database: ". mysqli_connect_error());
}
