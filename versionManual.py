from sys import exit
import math


def resuelve(mod, base):
    i = 1
    while True:
        if base ** i % mod == 1:
            return i
            break
        i = i + 1
        if i >= 400:  # Esto es una limitación del programa (NO DEL ALGORITMO) para evitar overflow
            return 0
            break


numero = int(input('Introduzca un número: '))
print('**************************************************************************')
print('**************************************************************************')
semilla = int(input('Introduce una semilla (2-{0}): '.format(numero - 1)))

while semilla:
    print('Semilla: {0}'.format(semilla))
    divisores = []
    candidato = math.gcd(numero, semilla)
    if candidato != 1:
        divisores.append(candidato)
        print('La semilla {0} produjo el factor: {1}'.format(semilla, divisores))
    else:
        r = resuelve(numero, semilla)
        if r == 0:
            print('Sospecho que {0} es primo'.format(numero))
        else:
            print('Periodo:', r)
            print('{0}^{1} mod {2} = 1'.format(semilla, r, numero))
            if r % 2 == 0:
                f1 = math.gcd(numero, semilla + r // 2)
                if f1 != 1 and f1 != numero:
                    divisores.append(f1)
                f2 = math.gcd(numero, abs(semilla - r // 2))
                if f2 != 1 and f2 != numero:
                    divisores.append(f2)
                if len(divisores) > 0:
                    print('Factores: {0}'.format(divisores))
                else:
                    print('Semilla inutil')
            else:
                print('Semilla inutil.')
    print('**************************************************************************')
    print('**************************************************************************')
    semilla = input('Introduce una semilla (2-{0}) o pulsa "e" para terminar: '.format(numero - 1))
    if semilla == 'e':
        exit()
    semilla = int(semilla)
