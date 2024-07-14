<!DOCTYPE html>
<html lang="es">
<head>
    <meta http-equiv="refresh" content="2">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sensor Ultrásonico</title>
    <meta charset="utf-8">
</head>
<body>
    <h1 style="text-align: center;"> Medición de Distancia: Sensor Ultrásonico HC-SR04 </h1>
    <?php
        // Ejecutar el script Python con los parámetros necesarios
        $comando = "sudo python3 /var/www/html/medir_distancias/distancia.py";

        // Ejecutar el comando y capturar la salida si es necesario
        $salida = shell_exec($comando);

        // Mostrar la salida o realizar alguna otra acción según sea necesario
        echo "<pre>$salida</pre>";

    ?>
    <h3 style="text-align: center; color: green;">Está página se actualizará cada 2 segundos.</h3>
</body>
</html>
