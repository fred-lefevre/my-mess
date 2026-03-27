<?php
$titre = "Introduction à PHP";
?>
<!DOCTYPE HTML>
<html lang="fr">

<head>
    <meta charset="UTF-8">
    <title><?= $titre ?></title>
</head>

<body>
    <h1><?= $titre ?></h1>
    <ul>
        <li><a href="bonjour.php">Hello world!</a></li>
        <li><a href="commentaire.php">Commentaires</a></li>
        <li><a href="typage-faible.php">Typage faible</a></li>
    </ul>
</body>

</html>