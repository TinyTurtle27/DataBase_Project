<?php

$host = "Localhost";
$user="root";
$pass= "Keter27#88M!";
$db="student_registration";

$conn=mysqli_connect($host, $user, $pass, $db);

if (!$conn) {
    die("Failed to connect to Database: ". mysqli_connect_error());
}
