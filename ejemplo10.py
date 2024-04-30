archivo  = open("data/atp_tennis.csv", "r")

lineas = archivo.readlines()

lineas = [l.split("|") for l in lineas]

for linea in lineas:
    torneo = linea[0]
    ganador = linea[9]

    contenido_html = f"""
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <title>Detalles del Torneo</title>
        </head>
        <body>
            <h1>Detalles del Torneo</h1>
            <p><strong>Torneo:</strong> {torneo}</p>
            <p><strong>Ganador:</strong> {ganador}</p>
        </body>
        </html>
        """

    nombre_archivo_html = f"data/{ganador.replace(' ', '_')}_en_{torneo.replace(' ', '_')}.html"

    with open(nombre_archivo_html, 'w', encoding='utf-8') as archivo_html:
        archivo_html.write(contenido_html)

print("Creados con exito")