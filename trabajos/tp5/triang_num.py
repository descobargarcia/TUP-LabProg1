print('\nGENERADOR DE TRIANGULO DE NUMEROS')
while True: 
    num = int(input('\nIngrese un entero positivo: '))
    if num <= 0:
        print('Numero invalido')
        continue
    else:
        break
print ()
for iterExt in range(1, num + 1):
    for iterInt in range (iterExt):
        print(iterInt + 1, end= ' ')
    print ()
