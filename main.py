import time
import psutil

# Obtém a quantidade atual de bytes enviados e recebidos
last_bytes_received = psutil.net_io_counters().bytes_recv
last_bytes_send = psutil.net_io_counters().bytes_sent
total_bytes = last_bytes_received + last_bytes_send

while True:
    # Obtém as quantidades atuais de bytes recebidos e enviados
    bytes_received = psutil.net_io_counters().bytes_recv
    bytes_send = psutil.net_io_counters().bytes_sent
    bytes_total = bytes_received + bytes_send

    # Calcula a diferença entre as quantidades atuais e as anteriores para obter os dados transmitidos no último segundo
    new_received = bytes_received - last_bytes_received
    new_send = bytes_send - last_bytes_send
    new_total = bytes_total - total_bytes

    # Converte as quantidades para MB
    mb_new_received = new_received / 1024 / 1024
    mb_new_send = new_send / 1024 / 1024
    mb_new_total  = new_total / 1024 / 1024

    # Imprime as quantidades em MB com duas casas decimais
    print(f"{mb_new_received:.2f} MB Recebidos, {mb_new_send:.2f} MB Enviados, {mb_new_total:.2f} MB total")

    # Atualiza as variáveis para as quantidades atuais
    last_bytes_received = bytes_received
    last_bytes_send = bytes_send
    total_bytes = bytes_total

    # Espera 1 segundo antes da próxima iteração
    time.sleep(1)
