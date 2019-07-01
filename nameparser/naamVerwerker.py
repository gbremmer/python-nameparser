from nameparser import HumanName as hn
from nameparser.config import CONSTANTS
import re


def verwerk_dubbele_geboortenaam(v_naam, a_naam):
    voornaam = v_naam
    achternaam = a_naam
    if ' geboren als' in voornaam:
        gesplitste_naam = [v for v in voornaam.split(' geboren als')]
    elif ', geboren' in voornaam:
        gesplitste_naam = [v for v in voornaam.split(', geboren')]
    elif 'geboren' in voornaam:
        gesplitste_naam = [v.strip(' ') for v in voornaam.split('geboren')]
    else:
        return(voornaam, achternaam)
    
    eerste_naam = hn(gesplitste_naam[0])
    if len(eerste_naam.middle) > 1:
        voornaam = eerste_naam.first.lower() + ' ' + eerste_naam.middle.lower()
    else:
        voornaam = eerste_naam.first.lower()
    achternaam = eerste_naam.last.lower() + ', geboren ' + achternaam
    return(voornaam, achternaam)


def naam_verwerker(input_naam):
    naam = hn(input_naam)
    achternaam = naam.last.lower()
    if len(naam.middle) > 1:
        voornaam = naam.first.lower() + ' ' + naam.middle.lower()
    else:
        voornaam = naam.first.lower()
        
    #Handle items with multiple birthnames
    if 'geboren' in voornaam:
        voornaam, achternaam = verwerk_dubbele_geboortenaam(voornaam, achternaam)
    
    prefix = ""
    
    for tussenvoegsel in CONSTANTS.prefixes:
    #for tussenvoegsel in PREFIXES: #lokaal prefixes 
        if re.search(r'\b' + tussenvoegsel.strip(' ') + r'\b', achternaam):
            if len(prefix) < len(tussenvoegsel):
                achternaam = naam.last[len(tussenvoegsel)+1:]
                prefix = tussenvoegsel
        
    return voornaam, prefix, achternaam
        
            

