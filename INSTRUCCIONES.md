# Convertidor de Cuentos .DOCX a JSON

## Instalación

1. Instalá Python (si no lo tenés): https://www.python.org/downloads/

2. Instalá la librería necesaria:
```bash
pip install python-docx
```

## Uso

1. **Creá una carpeta llamada `cuentos`** en el mismo lugar donde está el script

2. **Copiá todos tus archivos .docx** (tus 20 cuentos) dentro de esa carpeta

3. **Ejecutá el script:**
```bash
python convertir_cuentos.py
```

4. **Se genera automáticamente `cuentos.json`** con todos tus textos

## Estructura esperada:

```
tu-proyecto/
├── convertir_cuentos.py    ← El script
├── cuentos/                 ← Creás esta carpeta
│   ├── cuento1.docx
│   ├── cuento2.docx
│   ├── vorg-gombro.docx
│   └── kolon-3492.docx
└── cuentos.json             ← Se genera automáticamente
```

## Notas importantes:

- El **nombre del archivo** se usa como **título** en el menú
- Si querés cambiar los títulos después, editá el `cuentos.json`
- El script respeta saltos de línea y párrafos
- Archivos temporales de Word (~$.docx) se ignoran automáticamente

## Ejemplo de salida (cuentos.json):

```json
[
  {
    "title": "vorg-gombro",
    "text": "En el año 3492...\n\nLa nave colonial...\n\nLos primeros colonos..."
  },
  {
    "title": "kolon-3492",
    "text": "Kolón despertó...\n\nEl paisaje era extraño..."
  }
]
```

## Personalizar

Si querés cambiar el nombre de las carpetas, editá estas líneas en el script:

```python
convertir_carpeta_a_json(
    carpeta_entrada='cuentos',      # Cambiá acá el nombre de la carpeta
    archivo_salida='cuentos.json'   # Cambiá acá el nombre del JSON
)
```

## Solución de problemas

**Error: "No module named 'docx'"**
→ Ejecutá: `pip install python-docx`

**Error: "La carpeta 'cuentos' no existe"**
→ Creá la carpeta `cuentos` y poné tus .docx ahí

**No se encontraron archivos .docx**
→ Asegurate que los archivos tengan extensión .docx (no .doc)
