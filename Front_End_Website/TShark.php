<div class="box">
        <div class="box-header">
        <h1>End Points</h1>
        </div>
    
        <script> //Prevent Refresh Form Submission.
        if ( window.history.replaceState ) {
            window.history.replaceState( null, null, window.location.href );
        }
        </script>
        <br>
<?php

$host       = 'localhost';
$username   = 'wireshark';
$password   = 'wiresharkpassword';
$database   = 'wireshark';
$link = mysqli_connect($host, $username,$password ,$database );
if (!$link) {
    $output = 'Unable to connect to the database server.';
    echo "$output";
    exit();
}
if (!mysqli_select_db($link, $database)) {
    echo 'Unable to locate the database.';
    exit();
}
$output = 'Database connection established.';
echo "$output";

$result = mysqli_query($link, "SELECT * FROM edata");
echo "<table id='Table1Data' class='display nowrap' style='width:100%'>";
echo "
 <thead>
 <tr>

  <th>Address</th>
  <th>Packets</th>
  <th>Bytes</th>
  <th class='none'>Tx_Bytes</th>
  <th class='none'>Rx_Bytes</th>
  <th class='none'>Tx_Packets</th>
  <th class='none'>Rx_Packets</th>
  <th>First_Seen</th>
  <th>Last_Seen</th>
  <th>Organization</th>
  <th>Country</th>
  <th class='none'>Region</th>
  <th class='none'>City</th>
  </tr>
 </thead>
 <tbody>";

while ($row = mysqli_fetch_array($result)) {
    echo "<tr>";

    echo "<td >" . $row["Address"] . "</td>";
    echo "<td >" . $row["Packets"] . "</td>";
    echo "<td >" . $row["Bytes"] . "</td>";
    echo "<td >" . $row["Tx_Bytes"] . "</td>";
    echo "<td >" . $row["Rx_Bytes"] . "</td>";
    echo "<td >" . $row["Tx_Packets"] . "</td>";
    echo "<td >" . $row["Rx_Packets"] . "</td>";
    echo "<td >" . $row["First_Seen"] . "</td>";
    echo "<td >" . $row["Last_Seen"] . "</td>";
    echo "<td >" . $row["Organization"] . "</td>";
    echo "<td >" . $row["Country"] . "</td>";
    echo "<td >" . $row["Region"] . "</td>";
    echo "<td >" . $row["City"] . "</td>";

    echo "</tr>";
}

echo "</tbody></table></div>";

echo "<div class='box' >
<div class='box-header'>
<h1>End Point Updater</h1>
</div>

<form action='index.php' method='post'>
    <br>
    Address To Remove/Pull:<br>
    <input type='text' name='Address' placeholder='Address'required><br>
    <input type='submit' name='delete' value='DELETE'>
    <input type='submit' name='Pull' value='PULL'>
    </form>";

if (isset($_POST['delete'])) {
    $Address = $_POST['Address'];
    $query = "SELECT Address from edata where Address = '$Address'";
    $result = mysqli_query($link, $query);
    if ($result->num_rows == 0) {
        echo ("<h3 style='color:red'>Data Not Updated: DNI </h3>");
    } else {
        $query = "DELETE from edata where Address = '$Address'";
        $result = mysqli_query($link, $query);
        if ($result) {
            echo ("<h3 style='color:green'>Data Updated</h3>");
        } else {
            echo ("<h3 style='color:red'>Data Not Updated: " . mysqli_error($link) . "</h3>");
        }}
}
if (isset($_POST['Pull'])) {
    $Address = $_POST['Address'];
    $query = "SELECT * from edata where Address = '$Address'";
    $result = mysqli_query($link, $query);
    $row = mysqli_fetch_array($result);
    if ($result->num_rows == 0) {
        echo ("<h3 style='color:red'>Data Not Updated: DNI </h3>");
    } else {
        echo ("<h3 style='color:green'>Data Pulled</h3>");

        $Address = $row["Address"];
        $Packets = $row["Packets"];
        $Bytes = $row["Bytes"];
        $Tx_Bytes = $row["Tx_Packets"];
        $Tx_Packets = $row["Tx_Bytes"];
        $Rx_Packets = $row["Rx_Packets"];
        $Rx_Bytes = $row["Rx_Bytes"];
        $First_Seen = $row["First_Seen"];
        $Last_Seen = $row["Last_Seen"];
        $Organization = $row["Organization"];
        $Country = $row["Country"];
        $Region = $row["Region"];
        $City = $row["City"];

    }
}

echo "
  <form action='index.php' method='post'>
  <br>
    Address To Add:<br>
    <input type='text' name='Address' placeholder='Address'required value=" . $Address . "><br>
    <input type='number' name='Packets' placeholder='Packets'  min='0' value=" . $Packets . "><br>
    <input type='number' name='Bytes' placeholder='Bytes'  min='0' value=" . $Bytes . "><br>
    <input type='number' name='Tx_Bytes' placeholder='Tx_Bytes'  value=" . $Tx_Bytes . "><br>
    <input type='number' name='Rx_Bytes' placeholder='Rx_Bytes'  min='0' value=" . $Rx_Bytes . "><br>
    <input type='number' name='Tx_Packets' placeholder='Tx_Packets' min='0' value=" . $Tx_Packets . "><br>
    <input type='number' name='Rx_Packets' placeholder='Rx_Packets'  min='0' value=" . $Rx_Packets . "><br>
    <input type='text' name='First_Seen' placeholder='First_Seen'   value='" . $First_Seen . "'><br>
    <input type='text' name='Last_Seen' placeholder='Last_Seen'   value='" . $Last_Seen . "'><br>
    <input type='text' name='Organization' placeholder='Organization'   value='" . $Organization . "'><br>
    <input type='text' name='Country' placeholder='Country'   value='" . $Country . "'><br>
    <input type='text' name='Region' placeholder='Region'   value='" . $Region . "'><br>
    <input type='text' name='City' placeholder='City'   value='" . $City . "'><br>
    <input type='submit' name='ADD' value='ADD'>
    <input type='submit' name='Update' value='UPDATE'>
    </form>
  ";

if (isset($_POST['ADD'])) {
    $Address = $_POST['Address'];
    $Packets = $_POST['Packets'];
    $Bytes = $_POST['Bytes'];
    $Tx_Bytes = $_POST['Tx_Packets'];
    $Tx_Packets = $_POST['Tx_Bytes'];
    $Rx_Packets = $_POST['Rx_Packets'];
    $Rx_Bytes = $_POST['Rx_Bytes'];
    $First_Seen = $_POST['First_Seen'];
    $Last_Seen = $_POST['Last_Seen'];
    $Organization = $_POST['Organization'];
    $Country = $_POST['Country'];
    $Region = $_POST['Region'];
    $City = $_POST['City'];

    $query = "INSERT INTO edata (Address, Packets, Bytes, Tx_Packets, Tx_Bytes, Rx_Packets, Rx_Bytes, First_Seen, Last_Seen, Organization, Country, Region, City)
    VALUES('$Address', '$Packets', '$Bytes', '$Tx_Packets', '$Tx_Bytes', '$Rx_Packets', '$Rx_Bytes', '$First_Seen', '$Last_Seen', '$Organization', '$Country', '$Region', '$City')";
    $result = mysqli_query($link, $query);
    if ($result) {
        echo ("<h3 style='color:green'>Data Inserted");
    } else {
        echo ("<h3 style='color:red'>Data Not Updated: " . mysqli_error($link) . "</h3>");
    }
}

if (isset($_POST['Update'])) {
    $Address = $_POST['Address'];
    $Packets = $_POST['Packets'];
    $Bytes = $_POST['Bytes'];
    $Tx_Bytes = $_POST['Tx_Packets'];
    $Tx_Packets = $_POST['Tx_Bytes'];
    $Rx_Packets = $_POST['Rx_Packets'];
    $Rx_Bytes = $_POST['Rx_Bytes'];
    $First_Seen = $_POST['First_Seen'];
    $Last_Seen = $_POST['Last_Seen'];
    $Organization = $_POST['Organization'];
    $Country = $_POST['Country'];
    $Region = $_POST['Region'];
    $City = $_POST['City'];

    $query = "UPDATE edata
      SET
    Packets = '$Packets',
    Bytes ='$Bytes',
    Tx_Packets ='$Tx_Packets',
    Tx_Bytes='$Tx_Bytes',
    Rx_Packets ='$Rx_Packets',
    Rx_Bytes ='$Rx_Bytes',
    First_Seen ='$First_Seen',
    Last_Seen ='$Last_Seen',
    Organization ='$Organization',
    Country ='$Country',
    Region ='$Region',
    City ='$City'
    WHERE Address = '$Address'
    ";

    $result = mysqli_query($link, $query);
    if ($result) {
        echo ("<h3 style='color:green'>Data Updated");
    } else {
        echo ("<h3 style='color:red'>Data Not Updated: " . mysqli_error($link) . "</h3>");
    }
}

echo "</div>";

//Conversation Data Table
echo " <div class='box'>
<div class='box-header'>
<h1>Conversations</h1>
</div> ";
$result = mysqli_query($link, "SELECT * FROM cdata");
echo "<table id='Table2Data' style='width:100%' class='display' >
<thead><br>
 <tr>
  <th>Address_A</th>
  <th>Address_B</th>
  <th class='none'>Bytes_A_B</th>
  <th class='none'>Bytes_B_A</th>
  <th>Packets</th>
  <th>Bytes</th>
  <th>First_Seen</th>
  <th>Last_Seen</th>
 </tr>
 </thead>
 <tbody>";

while ($row = mysqli_fetch_array($result)) {

    echo "<tr>";
    echo "<td >" . $row["Address_A"] . "</td>";
    echo "<td >" . $row["Address_B"] . "</td>";
    echo "<td >" . $row["Bytes_A_B"] . "</td>";
    echo "<td >" . $row["Bytes_B_A"] . "</td>";
    echo "<td >" . $row["Packets"] . "</td>";
    echo "<td >" . $row["Bytes"] . "</td>";
    echo "<td >" . $row["First_Seen"] . "</td>";
    echo "<td >" . $row["Last_Seen"] . "</td>";
    echo "</tr>";
}

echo "</tbody></table></div>";
$link->close();

?>
