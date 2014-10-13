#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import sys
import os
from smallsmilhandler import SmallSMILHandler


class KaraokeLocal():

    def __init__(self, fichero):
        parser = make_parser()
        sHandler = SmallSMILHandler()
        parser.setContentHandler(sHandler)
        parser.parse(open(fichero))
        self.Lista = sHandler.get_tags()

    def do_local(self):
        for diccionario in self.Lista:
            for clave in diccionario:
                if clave != 'etiqueta' and diccionario[clave] != 'Null':
                    if clave == 'src':
                        os.system("wget -q " + diccionario[clave])
                        diccionario[clave] = diccionario[clave].split('/')[-1]

    def __str__(self):
        salida = ""
        for diccionario in self.Lista:
            salida += str('\n' + diccionario['etiqueta'] + '\t')
            for clave in diccionario:
                if clave != 'etiqueta' and diccionario[clave] != 'Null':
                    salida += str(clave + '="' + diccionario[clave] + '"\t')
        return salida

if __name__ == "__main__":

    try:
        fichero = sys.argv[1]
    except IndexError:
        sys.exit('Usage: python karaoke.py file.smil.')

    karaoke = KaraokeLocal(fichero)
    print karaoke
    karaoke.do_local()
    print karaoke
