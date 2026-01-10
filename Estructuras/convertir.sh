#!/bin/bash

# Bucle para procesar cada archivo html
for f in *.html; do
    # Obtenemos el nombre sin la extensión
    filename="${f%.*}"
    
    echo "Procesando: $f ..."
    
    # Ejecutamos pandoc con los filtros para limpiar el código
    # y conservar las fórmulas de MathJax ($$)
    pandoc "$f" \
        -f html \
        -t markdown+tex_math_dollars-native_spans \
        --wrap=none \
        -o "$filename.qmd"

    echo "Creado: $filename.qmd"
done

echo "---"
echo "Conversión finalizada. Recuerda revisar el contenido de los archivos .qmd"