#Fatorial de um numero 

numero_user = int(input('Digite um numero: '))
if numero_user > 0:
    fatorial = 1
    for item in range(1, numero_user + 1):
        fatorial = fatorial * item
    print(fatorial)