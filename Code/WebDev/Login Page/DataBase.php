<?php
require "config.php";

class DataBase
{
    public $connect;
    public $data;
    private $sql;
    protected $servername;
    protected $username;
    protected $password;
    protected $databasename;

    public function __construct()
    {
        $this->connect = null;
        $this->data = null;
        $this->sql = null;
        $dbc = new DataBaseConfig();
        $dbc->connect();
        $this->servername = $dbc->servername;
        $this->username = $dbc->username;
        $this->password = $dbc->password;
        $this->databasename = $dbc->databasename;
    }

    function dbConnect()
    {
        $this->connect = mysqli_connect($this->servername, $this->username, $this->password, $this->databasename);
        $this->sql = mysqli_stmt_init($this->connect);
        return $this->connect;
    }

    function Login($ID, $password){
        $sql_t = "select * from student where ID=?";

        if (!mysqli_stmt_prepare($this->sql, $sql_t)) { 
            header("Location: Login.php?error=codeFailed");
            exit;
        }

        mysqli_stmt_bind_param($this->sql,"s", $ID);
        mysqli_stmt_execute($this->sql);

        $result = mysqli_stmt_get_result($this->sql);
        if (mysqli_num_rows($result) > 0) {
            $row = mysqli_fetch_assoc($result);
            if ($row["Password"] == $password) {
                $_SESSION["ID"] = $row["ID"];

                header('Location: Registration.php');
                exit;
            }
        }

    }

    function getRegistration($ID) {
        $sql_t = "select * from Registration_List where ID_Student=?";

        if($this->sql == null) echo "this";

        if (!mysqli_stmt_prepare($this->sql, $sql_t)) { 
            header("Location: Login.php?error=FailLoginCourses");
            exit;
        }
        
        mysqli_stmt_bind_param($this->sql,"s", $ID);
        mysqli_stmt_execute($this->sql);

        $returned = array();
        $result = mysqli_stmt_get_result($this->sql);
        if (mysqli_num_rows($result) > 0) {
            $entry = array("Title"=>"Default", "Instructor"=>"Default", "Meeting"=>"Default", "Location"=>"Default");
            foreach ($result as $row) {
                    
                    // 
                    $sql_t = "select * from Section where ID=?";
                    mysqli_stmt_prepare($this->sql, $sql_t);

                    mysqli_stmt_bind_param($this->sql,"s", $row["ID_Section"]);

                    mysqli_stmt_execute($this->sql);
                    $result = mysqli_stmt_get_result($this->sql);
                    $sec = mysqli_fetch_assoc($result);
                    
                    $entry["Meeting"] = strval("M TH - ".$sec["Start_Time"] . "-". strval($sec["End_Time"]));

                    
                    
                    
                    
                    $room = $sec["ID_Room"];
                    $sql_t = "select * from Room where ID=?";
                    mysqli_stmt_prepare($this->sql, $sql_t);

                    mysqli_stmt_bind_param($this->sql,"s", $room);

                    mysqli_stmt_execute($this->sql);
                    $result = mysqli_stmt_get_result($this->sql);
                    $rom = mysqli_fetch_assoc($result);

                    
                    $sql_t = "select * from Building where ID=?";
                    mysqli_stmt_prepare($this->sql, $sql_t);

                    mysqli_stmt_bind_param($this->sql,"s", $rom['ID_Building']);

                    mysqli_stmt_execute($this->sql);
                    $result = mysqli_stmt_get_result($this->sql);
                    $bui = mysqli_fetch_assoc($result);

                    $entry["Location"] = "Rom: " . $rom['Number'] . " IN ". $bui["Title"];




                    // title 
                    $sql_t = "select * from course where ID=?";
                    mysqli_stmt_prepare($this->sql, $sql_t);

                    mysqli_stmt_bind_param($this->sql,"s", $sec['ID_Course']);

                    mysqli_stmt_execute($this->sql);
                    $result = mysqli_stmt_get_result($this->sql);
                    $course = mysqli_fetch_assoc($result);
                    $entry["Title"] = $course["Department"] .':'.strval($course["Num"]).' (' . strval($sec['ID']) .')     '. strval($course["Title"]);

                    // intercturo
                    $sql_t = "select * from Instructor where ID=?";
                    mysqli_stmt_prepare($this->sql, $sql_t);
                    mysqli_stmt_bind_param($this->sql,"s", $sec['ID_Instructor']);

                    mysqli_stmt_execute($this->sql);
                    $result = mysqli_stmt_get_result($this->sql);
                    $Instructor = mysqli_fetch_assoc($result);
                    $entry["Instructor"] = strval($Instructor["First_Name"]) . " " . strval($Instructor["Last_Name"]);
                    
                    // addition

                    $returned[] = $entry;
                
            }
            return $returned;
   
        }
    }
        
    }

?>