import re

def inverter(palavra):
    if re.match(r'^\w+$', palavra):
        return palavra[::-1]
    return palavra

frase = input("Digite a Frase:")
Frase_Invertida = ''.join(inverter(palavra) for palavra in re.split(r'(\W+)', frase))
print(Frase_Invertida)