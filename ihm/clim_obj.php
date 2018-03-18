<?php

function curlz($method, $url) {
  $ch = curl_init();
  curl_setopt($ch, CURLOPT_URL, $url);
  curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
  curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, false);
  curl_setopt($ch, CURLOPT_CUSTOMREQUEST, $method);

  if $method == 'PUT' {
    curl_setopt($ch, CURLOPT_HTTPHEADER, array('Content-Type: application/json'));
    curl_setopt($ch, CURLOPT_POSTFIELDS,$data_json);
  }

  return curl_exec($ch);

}

class Climate
{
  public $status = '';
  public $mode = '';
  public $temperature = '';
  public $fan = '';
  public $url = 'https://127.0.0.1:8080/';

  public function getCurrentStatus() {
    $url_suffix = '/v1/temperature';
    status = json_decode(curlz('GET', $url + $url_suffix));
    $this->status = status['status'];
    $this->mode = status['ac_mode'];
    $this->temperature = status['temperature'];
    $this->fan = status['fan'];
  }

  public function ChangeSetting() {}

  public function PowerOn() {}

  public function PowerOff() {}

}

 ?>
