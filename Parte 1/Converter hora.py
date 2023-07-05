import datetime


def convertHora(segundos):
    # Converter a data inicial em um objeto datetime
    data_inicial = datetime.datetime.strptime("06/01/1980 00:00:00", "%d/%m/%Y %H:%M:%S")
    # Converter o objeto datetime em segundos
    segundos_iniciais = data_inicial.timestamp()
    # Somar os segundos da data inicial com os segundos informados pelo usuário
    segundos_finais = segundos_iniciais + segundos
    # Converter os segundos em um objeto datetime
    return datetime.datetime.fromtimestamp(segundos_finais)

def horaBr(horaUTC):
    diferenca = datetime.timedelta(hours=3)
    return horaUTC - diferenca
    
# Pedir ao usuário o número de segundos
segundos = int(input("Digite o número de segundos: ")) #1256652800
data_final = convertHora(segundos)
# Mostrar a data e hora final na tela 
print(f"A data e hora em UTC      são {data_final.strftime('%d/%m/%Y %H:%M:%S')}")
# Calcular a diferença de 3 horas entre UTC e Brasília
brasilia = horaBr(data_final)
print(f"A data e hora em Brasília são {brasilia.strftime('%d/%m/%Y %H:%M:%S')}")

