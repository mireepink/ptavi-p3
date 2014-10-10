#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):

    def __init__(self):

        self.DiccionarioK = {
            'root-layout': ['width', 'height', 'background_color'],
            'region': ['id', 'top', 'bottom', 'left', 'rigth'],
            'img': ['src', 'region', 'begin', 'dur'],
            'audio': ['src', 'begin', 'dur'],
            'textstream': ['src', 'region']
        }
        self.Lista = []

    def startElement(self, etiqueta, attrs):

        if etiqueta in self.DiccionarioK:
            karaoke = {}
            karaoke['etiqueta'] = etiqueta
            for atributs in self.DiccionarioK[etiqueta]:
                karaoke[atributs] = attrs.get(atributs, 'Null')
            self.Lista.append(karaoke)

    def get_tags(self):
        return self.Lista

if __name__ == "__main__":

    parser = make_parser()
    sHandler = SmallSMILHandler()
    parser.setContentHandler(sHandler)
    parser.parse(open('karaoke.smil'))
    print sHandler.get_tags()
