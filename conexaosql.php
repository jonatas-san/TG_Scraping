<?php
$server_name ="localhost";
$username= "root";
$password= "Jessica@270221";
$datebase_name="scrapingapp";

$conn = mysqli_connect($server_name, $username, $password, $datebase_name);

if(!$conn){

    die("Falha na conexão: " . mysqli_connect_error());

}

if(isset($_POST['save']))
{
    $plchave = $_POST['plchave'];
    $dtinipl = $_POST['dtinipl'];
    $dtfimpl = $_POST['dtfimpl'];

    $sql_query = "INSERT INTO conexaosql (plchave, dtinipl, dtfimpl)
    VALUES ('$plchave', '$dtinipl', '$dtfimpl')";

    if(mysqli_query($conn, $sql_query))
    {
        echo "New Details Entry Inserted Successfully!";
    }
    else
    {
        echo "Error: " . $sql . "" . mysqli_error($conn);
    }
    mysqli_close($conn);

}
