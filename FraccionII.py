import itertools
import csv

# Listas basadas en la Fracción II
verbos = [
    'Oculte', 'encubra', 'pretenda ocultar', 'pretenda encubrir'
]

aspectos = [
    'la naturaleza', 'origen', 'ubicación', 'destino', 'movimiento', 'propiedad', 'titularidad'
]

objetos = [
    'recursos', 'derechos', 'bienes'
]

condiciones = [
    'cuando tenga conocimiento de que proceden de una actividad ilícita',
    'cuando tenga conocimiento de que representan el producto de una actividad ilícita'
]

# Intro fija
intro = "Se impondrá de cinco a quince años de prisión y de mil a cinco mil días multa al que, por sí o por interpósita persona realice"

# Generar combinaciones
combinaciones = []
for i, (verbo, aspecto, objeto, condicion) in enumerate(itertools.product(verbos, aspectos, objetos, condiciones), start=1):
    frase = f"{intro} {verbo} {aspecto} de {objeto}, {condicion}."
    combinaciones.append((i, frase))

# Escribir a CSV
filename = 'combinaciones_fraccion_II.csv'
with open(filename, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Número', 'Combinación'])
    writer.writerows(combinaciones)

print(f"Archivo '{filename}' generado con {len(combinaciones)} combinaciones.")