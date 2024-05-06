<?php
    include("DataBase.php");
    session_start();
    $db = new DataBase();
    $db->__construct();
    $conn = $db->dbConnect();
?>

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>DataBase Project</title>
  <link rel="stylesheet" href="login.css">
  <link href='https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css' rel='stylesheet'>
</head>


<body>

  <div class="wrapper">

    <form method="POST" action="Login.php">
      <i class='bx bxs-buildings'> COLWD</i>
      <h1>Login</h1>

      <div class="input-box">
        <input type="text" placeholder="Username" name="Username" required>
        <i class='bx bx-user'></i>
      </div>

      <div class="input-box">
        <input type="password" placeholder="Password" name="Password"required>
        <i class='bx bxs-lock-alt' ></i>
      </div>
      
      <button type="submit" class="btn">Login</button>
    </form>

  </div>
</body>
</html>

<?php
   if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $name = htmlspecialchars($_POST['Username']);
        $Pass = htmlspecialchars($_POST['Password']);

        $db->Login($name, $Pass) or die('');
    }
?>