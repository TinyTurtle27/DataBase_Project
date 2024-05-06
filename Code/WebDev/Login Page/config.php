<?php

class DataBaseConfig {
    
    public $servername;
    public $username;
    public $password;
    public $databasename;

    public function connect() {
        $this->servername = 'Localhost';
        $this->username = 'root';
        $this->password = 'Keter27#88M!';
        $this->databasename = "student_registration";

    }
}