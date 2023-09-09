<?php
// Define your MySQL database credentials
$host = "localhost";
$username = "jobs";
$password = "jobapplication";
$database = "applicants";

try {
    // Create a PDO connection to the MySQL database
    $pdo = new PDO("mysql:host=$host;dbname=$database", $username, $password);

    // Set the PDO error mode to exception
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    // Check if the form was submitted
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        // Retrieve form data
        $firstName = $_POST["firstName"];
        $lastName = $_POST["lastName"];
        $phone = $_POST["phone"];
        $email = $_POST["email"];
        $address = $_POST["address"];
        $formerEmployer = $_POST["formerEmployer"];
        $position = $_POST["position"];

        // SQL query with placeholders for prepared statement
        $sql = "INSERT INTO applicants (first_name, last_name, phone, email, address, former_employer, position) 
                VALUES (:firstName, :lastName, :phone, :email, :address, :formerEmployer, :position)";

        // Prepare the SQL statement
        $stmt = $pdo->prepare($sql);

        // Bind parameters to the placeholders
        $stmt->bindParam(":firstName", $firstName);
        $stmt->bindParam(":lastName", $lastName);
        $stmt->bindParam(":phone", $phone);
        $stmt->bindParam(":email", $email);
        $stmt->bindParam(":address", $address);
        $stmt->bindParam(":formerEmployer", $formerEmployer);
        $stmt->bindParam(":position", $position);

        // Execute the statement
        $stmt->execute();

        echo "Application submitted successfully!";
    }
} catch (PDOException $e) {
    echo "Error: " . $e->getMessage();
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Job Application Form</title>
</head>
<body>
    <h1>Job Application Form</h1>
    <form id="jobApplicationForm" action="" method="POST">
        <!-- The form fields (same as in the previous example) -->
        <!-- ... -->

        <!-- Submit Button -->
        <input type="submit" value="Submit">
    </form>
</body>
</html>

