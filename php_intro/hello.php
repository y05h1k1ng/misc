<!DOCTYPE html>
<head>
    <style>
        .center-text {
            text-align: center;
        }
    </style>
</head>
<html>
    <head>
        <title>PHP Test</title>
    </head>
    <form action="action.php" method="POST">
        <label for="name">名前：</label>
        <input name="name" id="name" type="text">

        <label for="age">年齢：</label>
        <input name="age" id="age" type="number">

        <button type="submit">Submit</button>
    </form>
    <body>
        <?php
        if (str_contains($_SERVER['HTTP_USER_AGENT'], 'Firefox')) {
        ?>
        <h3>You use Firefox.</h3>
        <?php
        } else {
        ?>
        <div class="center-text">
            <pre>
                What's??<br>
                <?php echo $_SERVER['HTTP_USER_AGENT']; ?>
            </pre>
        </div>
        <?php
        }
        ?>
    </body>
</html>