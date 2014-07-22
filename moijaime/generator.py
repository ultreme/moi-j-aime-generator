# -*- coding: utf-8 -*-

import random
import sys


wordlists = [
    [
        "manger",
        "dormir",
        "caresser",
        "rouler",
        "coller",
        "m'enduire",
        "marteau-piquer",
        "chanter",
        "arnaquer",
        "gratouiller",
        "tartiner",
        "applatir",
        "remplir",
        "compter",
        "dessiner",
        "nager",
        "reculer",
        "avancer",
        "patauger",
        "frire",
        "cuisiner",
        "defriser",
        "sandwicher",
        "palper",
        "denuder",
        "malaxer",
        "naviguer",
        "courir",
        "glouglouter",
        "attoucher",
        "arborer",
        "ostrehiculter",
        "chaloir",
        "balbutier",
        "corroborer",
        "contenter",
        "conchier",
        "chancir",
        "calfeutrer",
        "arnaquer",
        "dilater",
        "deblaterer",
        "deglinguer",
        "defequer",
        "eructer",
        "petrir",
        "frire",
        "glousser",
        "ejaculer",
        "procrastiner",
        "quiner",
        "creer",
        "vagir",
        "vomir",
    ], [
        "du vin",
        "du coca",
        "un singe",
        "de l'eau qui bulle",
        "un gredin",
        "un gentil-homme",
        "en belge",
        "en braille",
        "sans les mains",
        "pour de vrai",
        "a fond",
        "super vite",
        "en allemand",
        "des chips",
        "un sandwich",
        "une grand-mere",
        "le pere noel",
        "des merous",
        "un tournesol",
        "des resilles",
        "une bielle",
        "une biere",
        "jusqu'a Z",
        "en allemand",
        "un dictionnaire",
        "des nuages",
        "a Sonic",
        "des bougies",
        "mon clavier",
        "un poete",
        "un cucurbitace",
        "presque-surement",
        "un canard",
        "une grotte",
        "une crotte",
        "un ukulele",
        "un poulpe",
        "une patate",
        "une cruche",
        "une brouette",
        "la gaule",
        "une andouillette",
        "la frisette",
        "une sage-femme",
        "un sage-homme",
        "ta belle mere",
        "ta soeur",
        "du gruyere",
        "tes chaussettes",
        "le marquis",
        "le roi dagobert",
        "une photocopieuse",
        "des cartes pokemon",
        "une pomme",
        "une calculatrice",
        "du shampoing",
        "une syriane",
        "une pomme de terre",
        "par pitie",
        "une croute",
        "un groin",
        "le mot badaboum",
        "les tours de magies",
        "un chinois",
        "une dictature",
        "de la confiture",
        "une bagnolle",
        "100 balles et un mars",
        "les blagues",
        "un sphincter",
        "un pachiderme",
        "un reticule",
        "une poupee",
        "un lapin",
        "une boulette",
        "les spices girls",
        "les worlds appart",
        "les minikeums",
        "un cochon",
        "un berger",
        "un baton de berger",
        "un cable",
        "un camembert",
        "du saucisson",
        "une vis",
        "un ecrou",
        "un tournevis"
    ], [
        "orange",
        "mechant",
        "gonflable",
        "competent",
        "jaune",
        "gentil",
        "sympa",
        "rigolo",
        "top",
        "genial",
        "grand",
        "petit",
        "perime",
        "fatigue",
        "de toto",
        "du soir",
        None, None, None, None, None, None,
        None, None, None, None, None, None,
        None, None, None, None, None, None,
    ]
]


def generate_phrase(wordlists):
    phrase = ["Moi j'aime"]
    for wordlist in wordlists:
        word = random.choice(wordlist)
        if word:
            phrase.append(word)
    return phrase


def generate(lines):
    res = []
    for i in xrange(lines):
        res.append(' '.join(generate_phrase(wordlists)))
    return res


def main():
    lines = 10
    if len(sys.argv) > 1:
        lines = int(sys.argv[1])
    for line in generate(lines):
        print line

if __name__ == "__main__":
    main()