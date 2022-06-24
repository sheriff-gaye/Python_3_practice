#!/usr/bin/python3

#language detection funciton

def greet(language):
    lang = {
        'english': 'Welcome',
        'czech': 'Vitejte',
        'danish': 'Velkomst',
        'dutch': 'Welkom',
        'estonian': 'Tere tulemast',
        'finnish': 'Tervetuloa',
        'flemish': 'Welgekomen',
        'french': 'Bienvenue',
        'german': 'Willkommen',
        'irish': 'Failte',
        'italian': 'Benvenuto',
        'latvian': 'Gaidits',
        'lithuanian': 'Laukiamas',
        'polish': 'Witamy',
        'spanish': 'Bienvenido',
        'swedish': 'Valkommen',
        'welsh': 'Croeso'}
    
    
    if language=="":
        return "welcome"
    elif isinstance(language,int):
        return "welcome"
    elif  language not in lang:
        return "welcome"    
    else:
        arr=lang.get(language)
        return arr
print(greet('welsh'))
print(greet(2))
print(greet(''))
print(greet('IP_ADDRESS_INVALID'))