<!DOCTYPE HTML>
<html lang="fr">

<head>
    <meta charset="UTF-8">
    <title>Typage faible</title>
</head>

<body>
    <?php
    $v = 12;
    echo gettype($v) . "<br>";
    $v = true;
    echo gettype($v) . "<br>";
    $v = "Bobby";
    echo gettype($v) . "<br>";
    $v = 7.8;
    echo gettype($v) . "<br>";
    ?>
</body>

</html>