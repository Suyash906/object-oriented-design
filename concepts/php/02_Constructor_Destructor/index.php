<?php include_once ('includes/person.inc.php'); ?>
<!DOCTYPE html>
<html lang="en" dir="ltr">
    <head>
        <meta charset="utf-8">
        <title></title>
    </head>
    <body>
        <?php
            $person = new Person("Suyash", "Black", 27);
            echo $person->getName();
            echo $person->getEyeColor();
            echo $person->getAge();

            $person->setEyeColor("Blue");

            echo $person->getEyeColor();

        ?>
    </body>
</html>
