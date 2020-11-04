ano = 0
mes = 0
dia = 0

dias = int (input('Digite a idade em dias: '))

ano = (dias/365)
mes = (dias % 365) / 30
dia = (dias % 365) % 30

print("A idade em anos,meses e dias é:",ano,mes,dia)