def primo(n):
    if n > 1:
        for v in range(2,n):
            if n % v == 0:
                return False
        return True

def exibir():
    n=100
    for v in range(1,n+1):
        if(primo(v)):
            print("O número",v,"é Verdadeiro (É Primo!)")
        else:
            print("O número",v,"é Falso (Não é Primo!)")

exibir()