<?php
    session_start();
    include("connect.php");

    //check if form is submitted
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        //form data
        $selectedsubject = $_POST['selectedsubject'];
        $startselectedcomparison = $_POST['startselectedcomparison'];
        $start_time = $_POST['startselectedcomparisoninput'];
        $endselectedcomparison = $_POST['endselectedcomparison'];
        $end_time = $_POST['endselectedcomparisoninput'];
        $selectedgrouping = $_POST['selectedgrouping'];
        $selectedDays = $_POST['selectedDays'];
        $selectednamefilter = $_POST['selectednamefilter'];
        $instructor_lastname = $_POST['instructor_lastname'];
        $selectedcampus = $_POST['selectedcampus'];
        $selectedinstructionmethod = $_POST['selectedinstructionmethod'];

        // Create a prepared statement
        // NOTE MIGHT HAVE TO MAKE AN INNERJOIN OR SOME TYPE OF JOIN OF ALL RELEVANT TABLES FOR COURSE REGISTRATION
        $stmt = $conn->prepare("
            SELECT *
            FROM Course
            INNER JOIN Section ON Course.ID = Section.ID_Course
            INNER JOIN Room ON Section.ID_Room = Room.ID
            INNER JOIN Building ON Room.ID_Building = Building.ID
            INNER JOIN Instructor ON Section.ID_Instructor = Instructor.ID
            WHERE Course.Department = ?
        ");

        // Bind the selectedsubject parameter to the prepared statement
        $stmt->bind_param("s", $selectedsubject);

        // Execute the prepared statement
        $stmt->execute();

        // Get the result
        $result = $stmt->get_result();

        // Fetch all rows as an associative array
        $rows = $result->fetch_all(MYSQLI_ASSOC);

        // shows form data
        echo "<pre>";
        print_r($_POST);
        echo "</pre>";

        // Print all rows
        foreach ($rows as $row) {
            echo "<pre>";
            print_r($row);
            echo "</pre>";
        }
    }
?>

<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>DataBase Project</title>
    </head>

    <body>
        <p>sample text</p>
    </body>
</html>