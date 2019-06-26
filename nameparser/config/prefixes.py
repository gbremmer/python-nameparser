# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#: Name pieces that appear before a last name. They join with the following piece.
PREFIXES = set([
    'abu',
    'auf',
    'bon',
    'bin',
    'da',
    'dal',
    'de',
    'del',
    'dem',
    'der',
    'degli', # means "from" in Italian
    'de',
    'di',
    'dí',
    'du',
    'freiherrin', # See http://en.wikipedia.org/wiki/Ludwig_Freiherr_von_und_zu_der_Tann-Rathsamhausen
    'heer',
    'het',
    'in',
    'ibn',
    'la',
    'le',
    'op',
    'san',
    'st',
    'ste',
    # See http://www.dutchgenealogy.nl/tng/surnames-all.php
    'ten',
    'then',
    'tho',
    'thoe',
    'ter',
    'to',
    'van',
    'vande',
    # "vd" can be used to abbreviate "van de"/"van den"/"van der"
    # see http://en.wikipedia.org/wiki/List_of_most_common_surnames_in_Europe#Netherlands
    'vd', 
    'vel',
    'von',
    'und',
    'zu',
    "'t",
    'vander', 'auf der', 'onder de', "aan 't", 'uit het', 'wa', 'voor de', 'ben', "van 't", 'al', 'in ’t', 'voor den', 'aan de', 'op de', 'du', "voor in 't", 'zur', 'del', 'van der', 'des', "l'", 'van het', 'von', 'van t', 'de la', 'do', 'das', 'van den', 'de', 'op ’t', 'mc', 'da', "d'", 'van  der', 'uit den', "in 't", 'het', 'dos', 'de de', 'ten', 'olde', 'bij de', 'in de', 'la', 'in den', 'op den', 'ter', 'op', 'uit de', "'t", "in't", 'et', 'el', 'in het', 'te', 'di', 'der', 'de las', "op 't", 'a', 'le', 'van la', 'in der', 'van', 'den', 'op het', 'tho', 'van de',
])