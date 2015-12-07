#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""
Sencillo script en Python que da respuestas aleatorias, basado en la MagicBall8 (la que usa Millhouse en un capitulo de los Simpsons xD).

Escrito por: Gonza Cabrera.
"""

import random
import time

respuestas = ["En mi opinión SÍ","Es cierto","Decididamente así es","Probablemente","Buen pronóstico","Todo apunta a que sí","Sin duda","Sí","Sí - definitivamente","Debes confiar en ello","Mmmm...vuelve a intentarlo","Pregunta en otro momento","Será mejor que no te lo diga ahora","No puedo predecirlo ahora","Concéntrate y vuelve a preguntar","No cuentes con ello","Mi respuesta es no","Mis fuentes me dicen que no","Las perspectivas no son buenas","Muy dudoso"]

print "=== Bola Magica ==="
raw_input('Ingrese su pregunta: ')
print "================== \n"
print "[+] Agitando bola..."
time.sleep(2)
print "[+] ..."
time.sleep(2)
print "\n"
print "[" + (random.choice(respuestas)) + "]"
