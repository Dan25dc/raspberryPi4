<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Distancia consultas</title>
    <style>
        table {
            width: 100%;
            border-collapse: collapse;
        }
        table, th, td {
            border: 1px solid black;
            padding: 8px;
            text-align: left;
        }
        th {
            background-color: #f4d03f;
        }
        td{
            background-color: #ebdef0 ;
        }
    </style>
</head>
<body>
    <h1 style="text-align: center; color: blue">Consulta de datos</h1>
    <form action="" method="post">
        <p style="text-align: center;">Buscar&nbsp;&nbsp;
            <input type="text" name="busqueda" size="20" maxlength="20" value="Todos">&nbsp;
            <select name="tipoBusqueda">
                <option value="todos" selected>Todo</option>
                <option value="distancia">Distancia</option>
                <option value="fecha">Fecha</option>
                <option value="hora">Hora</option>
                <option value="count">Total de datos</option>
                <option value="max">Distancia Máxima</option>
                <option value="min">Distancia Mínima</option>
                <option value="avg">Promedio de distancias</option>
            </select>
            <input type="submit" name="buscar" value="Buscar">
        </p>
    </form> 
    
    <?php
        if ($_SERVER["REQUEST_METHOD"] == "POST") {
            // Obtener los valores del formulario
            $busqueda = $_POST["busqueda"];
            $tipoBusqueda = $_POST["tipoBusqueda"];

            // Construir el comando para ejecutar el script Python
            $comando = "sudo python3 /var/www/html/consultar_distancias/distancias.py \"$busqueda\" \"$tipoBusqueda\"";

            // Ejecutar el comando y capturar la salida
            $salida = shell_exec($comando);

            // Mostrar la salida en una tabla si hay resultados
            if (!empty($salida)) {
                echo "<h2>Resultados:</h2>";
                if ($tipoBusqueda == "count" || $tipoBusqueda == "max" || $tipoBusqueda == "min" || $tipoBusqueda == "avg") {
                    // Si es una consulta que devuelve un solo valor
                    echo "<p>{$salida}</p>";
                } else {
                    // Si son múltiples registros
                    $registros = json_decode($salida, true); // Decodificar JSON a array asociativo
                    if (!empty($registros)) {
                        // Encabezados de la tabla
                        echo "<table>";
                        echo "<tr><th>DISTANCIA (CM)</th><th>FECHA</th><th>HORA</th></tr>";
                        // Filas de datos
                        foreach ($registros as $registro) {
                            $distancia = $registro['CM'];
                            $fecha = $registro['FECHA'];
                            $hora = $registro['HORA'];
                            echo "<tr><td>{$distancia}</td><td>{$fecha}</td><td>{$hora}</td></tr>";
                        }
                        echo "</table>";
                    } else {
                        echo '<h3 style="color: red">No se encontraron resultados.</h3>';
                    }
                }
            } else {
                echo "<p>No se obtuvieron resultados.</p>";
            }
        }
    ?>
</body>
</html>
