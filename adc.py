# adc.py
import time
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import RPi.GPIO as GPIO

def initialize_ads(pin_power_gpio=26):
    """
    Inicjalizuje GPIO oraz ADS1015 i zwraca obiekt AnalogIn dla kanału 0.
    """
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin_power_gpio, GPIO.OUT)
    GPIO.output(pin_power_gpio, GPIO.HIGH)

    i2c = busio.I2C(board.SCL, board.SDA)
    ads = ADS.ADS1015(i2c)
    chan = AnalogIn(ads, ADS.P0)
    return chan

def read_voltage(chan):
    """
    Zwraca zmierzone napięcie z podanego kanału ADS1015.
    """
    return chan.voltage

def cleanup_gpio():
    """
    Czyści ustawienia GPIO.
    """
    GPIO.cleanup()

if __name__ == "__main__":
    try:
        chan = initialize_ads()
        while True:
            voltage = read_voltage(chan)
            print(f"Napięcie: {voltage:.2f} V")
            time.sleep(1)
    finally:
        cleanup_gpio()
