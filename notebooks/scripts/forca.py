import os


print('---- JOGO DA FORCA ----')

palavra = 'livro'
palavra_digitada = '_' * len(palavra)

print('----|')
print('|')
print('|')
print('|')
print(palavra_digitada, end = ' ')
print('\n\n')
chances = 5  # ou len(set(palavra))
for chance in range(chances):
    print(f'Você tem {chances - chance} chances.\n')
    letra_digitada = input("Letra: ")

    for posicao, letra in enumerate(palavra):
        if letra_digitada == letra:
            # acertou uma letra!
            palavra_digitada = palavra_digitada[:posicao] + letra + palavra_digitada[posicao+1:]
    os.system('clear')
    print('----|')
    print('|')
    print('|')
    print('|')
    print(palavra_digitada, end = ' ')
    print('\n\n')

if palavra_digitada != palavra:
    print(f'Você perdeu :( A palavra era: {palavra} e você completou: {palavra_digitada}')
else:
    print(f'Você acertou! {palavra_digitada}')
