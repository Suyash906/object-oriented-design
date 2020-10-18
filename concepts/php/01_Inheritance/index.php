<!DOCTYPE html>
<html lang="en" dir="ltr">
    <head>
        <meta charset="utf-8">
        <title></title>
    </head>
    <body>
        <?php
            include_once ('includes/person.inc.php');
            $pet01 = new Pet();

            echo $pet01->owner();
        ?>
    </body>
</html>
