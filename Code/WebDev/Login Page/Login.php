<?php
    session_start();

    include("connect.php");
    include("Functions.php");

    if($_SERVER['REQUEST_METHOD'] == "POST") {
        $user_name = $_POST["UID"];
        $password = $_POST["PWD"];

        if (!empty($user_name) && !empty($password)) {
            $query = "select * from student where ID = $user_name limit 1";
            
            $result = mysqli_query($conn, $query) or die(mysqli_error($conn));

            if($result) {
                if(mysqli_num_rows($result) > 0) { 
                    $row = mysqli_fetch_array($result);
                    header ("Location: web.php");
                }
            }
        }
    }
?>

<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>DataBase Project</title>
        <link rel="stylesheet" href="Log.css">
    </head>

    <body>

        <div class="wrapper">

            <form method="post" action="">
                <div class="input-box">
                    <input type="text" name="UID" placeholder="Username" required>
                </div>

                <div class="input-box">
                    <input type="Password" name="PWD" placeholder="Password" required>
                </div>

                <div class="Register-Student">
                    <p>
                        Admin: <a href="">Register Student</a>
                    </p>
                </div>
                <div class="Button">
                    <button type="submit" class="btn" name="submit"><a href="C:\Users\ORA PC\Desktop\Repos\DataBase_Project\Code\WebDev\others\web.php"></a>Login</button>
                </div>
            </form>


        </div>

    </body>
</html>