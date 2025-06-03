import loralib         
import time  
import adc
import gps

# Inicjalizacja LoRa
loralib.init(0, 434000000, 7) 
# Inicjalizacja ADC
potencjometer = adc.initialize_ads()

while True:

    log = "Jestem logiem"
    message = ""
    
    # coords = gps.get_coordinates()
    coords = (51.1287, 17.044)
    if coords:
        print("Współrzędne:", coords)
        message += f"{coords[0]};{coords[1]};"
    else:
        log = "Nie udało się uzyskać współrzędnych GPS."
        print(log)
        message = " ; ;"

    voltage = adc.read_voltage(potencjometer)

    message += f"{voltage:.2f};"

    if log != "":
        message += "!" + log 

    print(message)
    loralib.send(str(message).encode())
    time.sleep(3)