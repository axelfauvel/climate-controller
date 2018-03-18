<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <link rel="stylesheet" href="style.css" />
        <title>Réglage clim salon</title>
    </head>

<div class="row">
  <div class="column">
    <span class="power">
        <p>Allumer / éteindre</p>
        <a href="power.php?power=poweron">ON</a><br>
        <a href="power.php?power=poweroff">OFF</a>
    </span>
  </div>

  <div class="column">
      <span class="status">
      <p>Réglage actuel <br>

          <?php

            $url="https://127.0.0.1:8080/v1/temperature";

            $ch = curl_init();
            curl_setopt($ch, CURLOPT_URL, $url);
            curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
            curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, false);
            curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);


            $result  = curl_exec($ch);
            if (!$result) {
                die("Connection Failure.n");
            }
            curl_close($ch);


            $data = json_decode($result, true);


            if ($data['ac_mode'] == 'heat') {
                print('<font color="#FF3333" size="12vw">' . $data['temperature'] . '</font>');
            }
            elseif ($data['ac_mode'] == 'clim') {
                print('<font color="#00BFFF" size="12vw">' . $data['temperature'] . '</font>');
            }


            ?>

          </p>
  </span>
  </div>

</div>


<div class="row">
  <div class="column">
      <span class="chauffage">
          <p>Chaud</p>
        <a href="climate.php?ac_mode=heat&temperature=18">18</a><br>
        <a href="climate.php?ac_mode=heat&temperature=19">19</a><br>
        <a href="climate.php?ac_mode=heat&temperature=20">20</a><br>
        <a href="climate.php?ac_mode=heat&temperature=21">21</a><br>
        <a href="climate.php?ac_mode=heat&temperature=22">22</a><br>
        <a href="climate.php?ac_mode=heat&temperature=23">23</a><br>
        <a href="climate.php?ac_mode=heat&temperature=24">24</a><br>
        <a href="climate.php?ac_mode=heat&temperature=25">25</a><br>
      </span>
  </div>

  <div class="column">
      <span class="clim">
          <p>Clim</p>
        <a href="climate.php?ac_mode=clim&temperature=18">18</a><br>
        <a href="climate.php?ac_mode=clim&temperature=19">19</a><br>
        <a href="climate.php?ac_mode=clim&temperature=20">20</a><br>
        <a href="climate.php?ac_mode=clim&temperature=21">21</a><br>
        <a href="climate.php?ac_mode=clim&temperature=22">22</a><br>
        <a href="climate.php?ac_mode=clim&temperature=23">23</a><br>
        <a href="climate.php?ac_mode=clim&temperature=24">24</a><br>
        <a href="climate.php?ac_mode=clim&temperature=25">25</a><br>
      </span>
  </div>
</div>


</html>