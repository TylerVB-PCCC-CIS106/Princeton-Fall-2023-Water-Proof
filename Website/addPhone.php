<?php  
$phone = $_POST["phoneNum"];
$fp = fopen('phones.txt', 'a');//opens file in append mode  
fwrite($fp, "1".$phone."\n");  
fclose($fp);  
  
echo "Phone Added!";  
?>  