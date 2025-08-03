import itertools
import csv

# Listas basadas en la Fracción I
verbos = [
    'Adquiera', 'enajene', 'administre', 'custodie', 'posea', 'cambie', 'convierta',
    'deposite', 'retire', 'dé por cualquier motivo', 'reciba por cualquier motivo',
    'invierta', 'traspase', 'transporte', 'transfiera'
]

ubicaciones = [
    'dentro del territorio nacional', 'de éste hacia el extranjero', 'a la inversa'
]

objetos = [
    'recursos', 'derechos', 'bienes de cualquier naturaleza'
]

condiciones = [
    'cuando tenga conocimiento de que proceden de una actividad ilícita',
    'cuando tenga conocimiento de que representan el producto de una actividad ilícita'
]

# Intro fija
intro = "Se impondrá de cinco a quince años de prisión y de mil a cinco mil días multa al que, por sí o por interpósita persona realice"

# Generar combinaciones
combinaciones = []
for i, (verbo, ubicacion, objeto, condicion) in enumerate(itertools.product(verbos, ubicaciones, objetos, condiciones), start=1):
    frase = f"{intro} {verbo} {ubicacion}, {objeto}, {condicion}."
    combinaciones.append((i, frase))

# Escribir a CSV
filename = 'combinaciones_fraccion_I.csv'
with open(filename, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Número', 'Combinación'])
    writer.writerows(combinaciones)

print(f"Archivo '{filename}' generado con {len(combinaciones)} combinaciones.")