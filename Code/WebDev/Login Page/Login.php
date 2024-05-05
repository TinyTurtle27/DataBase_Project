<?php
    session_start();

    $_SESSION;

    include("connect.php");
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

            <form method="post" action="Functions.php">
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
                    <button type="submit" class="btn" name="submit"><a href="Login.php"></a>Login</button>
                </div>
            </form>


        </div>

    </body>
</html>