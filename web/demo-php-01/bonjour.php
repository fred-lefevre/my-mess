<?php
$prenom = "Bill";
$age = 18;
?>
<!DOCTYPE HTML>
<html lang="fr">

<head>
    <meta charset="UTF-8">
    <title>Hello</title>
</head>

<body>
    <h1>Hello <?php echo $prenom; ?></h1>
    <?php
    if ($age >= 18) {
        echo "<p>Tu es officiellement un adulte</p>";
    } else {
        echo "<p>Tu n'es pas un adulte</p>";
    }
    ?>
</body>

</html>