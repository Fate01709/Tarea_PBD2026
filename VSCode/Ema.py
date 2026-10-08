from datetime import datetime

with open('Diario.txt', 'a') as Entrada:
    Entrada.write(f'[{datetime.now().strftime("%Y-%m-%d %H:%M")}]: ')