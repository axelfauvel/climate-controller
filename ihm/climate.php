<?php

$temperature=$_GET['temperature'];
$ac_mode=$_GET['ac_mode'];
$url="https://127.0.0.1:8080/v1/temperature";


$data = array('ac_mode'=>$ac_mode,'temperature'=>$temperature,'fan'=>'auto');
$data_json = json_encode($data);


$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_HTTPHEADER, array('Content-Type: application/json'));
curl_setopt($ch, CURLOPT_CUSTOMREQUEST, 'PUT');
curl_setopt($ch, CURLOPT_POSTFIELDS,$data_json);
#curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, false);



$response  = curl_exec($ch);
if (!$response) {
    die("Connection Failure.n");
}
curl_close($ch);
header("Location: http://192.168.1.27");
exit();

?>