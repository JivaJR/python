import random
import os

VALIDOPTIONS = ['piedra','papel','tijeras']

victoriashumano = 0
victoriasmachine = 0
empates = 0

jugar = 0
isValid = 0
select=''

while jugar == 0:
    os.system('cls')
    machine = random.choice(VALIDOPTIONS)
    while isValid == 0:
        if select in VALIDOPTIONS:
            human = select
            break
        human = input('Selecciona: Piedra,papel o tijeras juega humano:\n')
        human = human.lower()
        if human in VALIDOPTIONS:
            isValid=1
        else:
            print(f"{human} No es un valor valido.")

    if human == machine:
        print(f'Empatamos con {human}')
        empates=empates+1

    elif human == 'papel' and machine == 'piedra' or human == 'tijeras' and machine == 'papel' or human == 'piedra' and machine == 'tijeras':
        print(f'Felicidades, le ganaste a mi {machine} con {human}')
        victoriashumano = victoriashumano + 1
    else:
        print(f'JAJAJA, Fallaste humano le gane a tu {human} con {machine}')
        victoriasmachine = victoriasmachine + 1
    print(f'Hasta ahora llevo {victoriasmachine} victorias y tu {victoriashumano} victorias y hemos empatado {empates} veces')
    select = input('¿Deseas seguir jugando? (Y/N)\n')
    if select.lower() == 'y' or select.lower() in VALIDOPTIONS:
        print('Muy bien, sigamos')
        isValid=0
    else:
        print(f'Tomare tu {select} como una forma de decir que no quieres jugar jajajajaj. No pudiste con mi poder JAJAJAJAJ. Entrena y vuelve pronto')
        jugar = 1