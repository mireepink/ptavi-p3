#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import sys
from smallsmilhandler import SmallSMILHandler


class Karaoke(SmallSMILHandler):

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

parser = make_parser()
sHandler = Karaoke()
parser.setContentHandler(sHandler)
parser.parse(open(fichero))
print sHandler
