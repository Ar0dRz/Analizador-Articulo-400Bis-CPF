# Analizador-Articulo-400Bis-Código Penal Federal (México)
Herramienta para generar combinaciones exhaustivas de artículos de ley (ej: Art. 400 Bis CPF sobre lavado de dinero). [Código Penal](https://www.diputados.gob.mx/LeyesBiblio/pdf/CPF.pdf)

# Generador de Combinaciones Legales

Herramienta para generar combinaciones de los artículos de ley, como el Artículo 400 Bis del Código Penal Federal (sobre lavado de dinero y encubrimiento). Útil para análisis legales, estudios o auditorías. Incluye scripts para Python, más CSVs con ejemplos generados.

## Propósito
Este repo desglosa artículos en listas de verbos, objetos, condiciones, etc., y genera todas las permutaciones posibles. Ejemplo: Para Fracción I, produce 270 variantes; para II, 168. Basado en un macro VBA original para un artículo similar.

## Archivos incluidos

- **generar_fraccion_I.py**: Script Python para Fracción I del Art. 400 Bis (genera CSV con 270 combinaciones).
- **generar_fraccion_II.py**: Script Python para Fracción II (genera CSV con 168 combinaciones).
- **combinaciones_fraccion_I.csv** y **combinaciones_fraccion_II.csv**: Resultados generados, listos para importar a Excel.

## Cómo usarlo
### Con Python
1. Instala Python (si no lo tienes).
2. Ejecuta `python Fraccion_I.py` – genera el CSV automáticamente.
3. Abre el CSV en Excel para ver las combinaciones.


**Requisitos**: Python 3+ para scripts .py. Esto es para fines educativos – no sustituye asesoría legal.

## Ejemplo de combinación (Fracción I)
Se impondrá de cinco a quince años de prisión y de mil a cinco mil días multa al que, por sí o por interpósita persona realice Adquiera dentro del territorio nacional, recursos, cuando tenga conocimiento de que proceden de una actividad ilícita.

## Contribuciones
Si agregas más artículos o mejoras, haz un pull request.

## Licencia
MIT – Usa libremente, pero cita la fuente.
