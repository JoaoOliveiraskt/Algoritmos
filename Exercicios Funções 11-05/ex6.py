def converter_hora(horas, minutos):
    if horas >= 0 and horas <= 11:
        momento = 'A.M'
        if horas == 0:
            horas = 12
    else:
        momento = 'P.M'
        if horas != 12:
            horas -= 12
    return horas, minutos, momento   

def mostrar_hora(horas, minutos, momento):
    print("O horário convertido é: {}:{} {}".format(horas, minutos, momento))     

while True:
    horas = int(input("Digite as horas: "))
    minutos = int(input("Digite os minutos: "))
    horario12h = converter_hora(horas, minutos)
    mostrar_hora(*horario12h)
    repitir_calculo = (input("Deseja converter outro horário? (s/n) "))
    if repitir_calculo.lower() != 's':
        break