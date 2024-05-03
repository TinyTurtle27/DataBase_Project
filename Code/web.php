<?php
    session_start();
    include("trash.php");
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div>Other included later</div>
    
    <div class="Registered Classes">
        <table class="outer table" brder="True">
            <caption>
                <h3>Registered Classes</h3>
                <h4>Term: Fall 2020</h4>
            </caption>

            <thead>
                <tr>
                    <th>Title</th>
                    <th>Instructor</th>
                    <th>Meeting Time</th>
                    <th>Status</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>testing</td>
                    <td>
                        <?php
                            $query = $pdo->query('select * from student');
                            $data = $query->fetchAll(PDO::FETCH_NUM);
                            if ($data) {
                                echo $data[0][2];
                            } else { 
                                ?>
                                NA
                                <?php
                            }

                        ?>
                    </td>
                    <td>
                        <table border="True">
                            <tr>
                                <th>M</th>
                                <th>T</th>
                                <th>W</th>
                                <th>TH</th>
                                <th>F</th>
                            </tr>
                        </table>
                    </td>
                    <td>Registed</td>
                </tr>
                <tr>
                    <td>tt</td>
                    <td>d</td>
                    <td>
                        <table border="True">
                            <tr>
                                <th>M</th>
                                <th>T</th>
                                <th>W</th>
                                <th>TH</th>
                                <th>F</th>
                            </tr>
                        </table>
                    </td>
                    <td>w</td>
                </tr>
            </tbody>
        </table>
    </div>
</body>
</html>