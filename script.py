
import csv

archivo_csv = "events.csv"      # tu archivo de entrada
archivo_salida = "eventos.qmd" # archivo de salida

bloques = []

with open(archivo_csv, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        date = row["date"]
        event = row["event"]
        image = row["image"]
        label = row["label"]

        # ancla para Closeread, siguiendo el patrón cr-label
        anchor = f"cr-{label}"

        bloque = f""":::{{.cr-section}}

{date} @{anchor}

:::{{#{anchor}}}
{event}
![]({image}){{width=30%}}
:::

:::

"""
        bloques.append(bloque)

contenido = "\n".join(bloques)

with open(archivo_salida, "w", encoding="utf-8") as f:
    f.write(contenido)
