<?php

$servername = "Kenya Capital Markets";
$username = "YoungKE";
$password = "W42721218f";
$dbname = "database.sql";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

// SQL query
$sql = "SELECT * FROM users";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
  // Output data of each row
  while($row = $result->fetch_assoc()) {
    echo "id: " . $row["id"]. " - Name: " . $row["name"]. " " . $row["email"]. "<br>";
  }
} else {
  echo "0 results";
}
$conn->close();


function generateUniqueReferralCode($length = 8) {
    $characters =
    'ABCDEFGHJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    $string = ";
    $max = strlen($characters) -1;
    for($i = 0; $i <$length;$i++) {
        $string .=$characters[mt_rand(0,$max)];

}

//Check for uniqueness in the database

$db = connectToDatabase();
$sql = "SELECT COUNT(*) FROM users WHERE referral_code = ?";
$stmt = $db->prepare($sql);
$stmt->bind_param("s", $string);
$stmt->execute();
$result = $stmt->get_result();
$row = $result->fetch_assoc();

if ($row['COUNT(*)']>0){
    //If not unique, generate another code recursively

    return generateUniqueReferralCode($length);
}

return $string
}

function createUser($username,$password,$email){
    $db = connectToDatabase();
    $hashedPassword = password_hash($password, PASSWORD_DEFAULT);
    $referralCode = generateUniqueReferralCode();

    $sql = "INSERT INTO users (username,password,email,referral_code) VALUES (?,?,?,?)";
    $stmt = $db ->prepare($sql);
    $stmt->bind_param("ssss",$username, $hashedPassword,$email,$referralCode;
    $stmt->execute();


    return $stmt->affected_rows> 0;
}

//Example usage

if (isset($_POST['username'])&&
isset($_POST['password']) && isset($_POST['email'])){
    $username = $_POST['username'];
    $password = $_POST['password'];
    $email = $_POST['email'];


    if (createUser($username,$password,$email)){
        echo "User created sucessfully with referral code:
    " . generateUniqueReferralCode();
    } else {
        echo "Failed to create user
        Try again.";
    }
}

?>



 