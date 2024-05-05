<?php
    session_start();

    $_SESSION;

    include("trash.php");
?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="Log.css">
</head>

<body>

    <div class="wrapper">

        <form method="post" >
            <div class="input-box">
                <input type="text" placeholder="Username" required>
            </div>

            <div class="input-box">
                <input type="Password" placeholder="Password" required>
            </div>

            <div class="Register-Student">
                <p>
                    Admin: <a href="">Register Student</a>
                </p>
            </div>
        </form>

        <div class="Button">
            <button type="submit" class="btn"><a href="Login.php"></a>Login</button>
        </div>
    </div>

</body>
</html>