#!/usr/bin/env python3
"""
Script para convertir archivos .docx a formato JSON para el lector de cuentos.

Uso:
1. Poné todos tus archivos .docx en una carpeta llamada 'cuentos'
2. Ejecutá: python convertir_cuentos.py
3. Se genera cuentos.json automáticamente
"""

import json
import os
from pathlib import Path

try:
    from docx import Document
except ImportError:
    print("❌ Error: Necesitás instalar python-docx")
    print("Ejecutá: pip install python-docx")
    exit(1)


def extraer_texto_docx(archivo_path):
    """Extrae todo el texto de un archivo .docx"""
    try:
        doc = Document(archivo_path)
        texto_completo = []
        
        for parrafo in doc.paragraphs:
            if parrafo.text.strip():  # Solo agregar párrafos no vacíos
                texto_completo.append(parrafo.text.strip())
        
        return '\n\n'.join(texto_completo)
    
    except Exception as e:
        print(f"⚠️  Error leyendo {archivo_path}: {e}")
        return None


def convertir_carpeta_a_json(carpeta_entrada='cuentos', archivo_salida='cuentos.json'):
    """Convierte todos los .docx de una carpeta a JSON"""
    
    carpeta = Path(carpeta_entrada)
    
    if not carpeta.exists():
        print(f"❌ La carpeta '{carpeta_entrada}' no existe")
        print(f"Creá una carpeta llamada '{carpeta_entrada}' y poné tus archivos .docx ahí")
        return
    
    # Buscar todos los archivos .docx
    archivos_docx = list(carpeta.glob('*.docx'))
    archivos_docx = [f for f in archivos_docx if not f.name.startswith('~$')]  # Ignorar archivos temporales
    
    if not archivos_docx:
        print(f"❌ No se encontraron archivos .docx en '{carpeta_entrada}'")
        return
    
    print(f"📚 Encontrados {len(archivos_docx)} archivos .docx")
    print()
    
    cuentos = []
    
    for archivo in sorted(archivos_docx):
        print(f"📖 Procesando: {archivo.name}")
        
        # Extraer el título del nombre del archivo (sin extensión)
        titulo = archivo.stem
        
        # Extraer el texto
        texto = extraer_texto_docx(archivo)
        
        if texto:
            cuentos.append({
                'title': titulo,
                'text': texto
            })
            print(f"   ✅ {len(texto)} caracteres extraídos")
        else:
            print(f"   ⚠️  No se pudo extraer texto")
        
        print()
    
    if cuentos:
        # Guardar como JSON
        with open(archivo_salida, 'w', encoding='utf-8') as f:
            json.dump(cuentos, f, ensure_ascii=False, indent=2)
        
        print(f"✨ ¡Listo! Se creó '{archivo_salida}' con {len(cuentos)} cuentos")
        print(f"📦 Tamaño del archivo: {os.path.getsize(archivo_salida) / 1024:.1f} KB")
        print()
        print("🚀 Ahora podés:")
        print(f"   1. Subir '{archivo_salida}' a tu repo de GitHub")
        print("   2. Actualizar el HTML para que cargue desde ese JSON")
    else:
        print("❌ No se pudo convertir ningún archivo")


if __name__ == '__main__':
    print("=" * 60)
    print("  CONVERTIDOR DE CUENTOS .DOCX → JSON")
    print("=" * 60)
    print()
    
    convertir_carpeta_a_json()
