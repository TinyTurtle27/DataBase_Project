<?php
include("Connect.php");

if(isset($_POST["submit"])){
    $Username = $_POST["UID"];
    $Password = $_POST["PWD"];


} else {
    header("Location: Login.php");
}

