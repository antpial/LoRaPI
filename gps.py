# gps_module.py

import serial
import pynmea2

def get_coordinates(port="/dev/serial0", baudrate=9600, timeout=1):
    """
    Pobiera współrzędne geograficzne z modułu GPS.
    Zwraca:
        dict: {'latitude': ..., 'longitude': ...} jeśli uda się odczytać
        None: jeśli brak danych lub wystąpił błąd
    """
    try:
        with serial.Serial(port, baudrate, timeout=timeout) as ser:
            for _ in range(10):  # próbuj maks. 10 linii
                line = ser.readline().decode('utf-8', errors='ignore').strip()
                if line.startswith('$GPRMC') or line.startswith('$GNRMC'):
                    try:
                        msg = pynmea2.parse(line)
                        if hasattr(msg, 'latitude') and hasattr(msg, 'longitude'):
                            return {
                                'latitude': f"{msg.latitude} {msg.lat_dir}",
                                'longitude': f"{msg.longitude} {msg.lon_dir}"
                            }
                    except pynmea2.ParseError:
                        continue
    except Exception as e:
        print(f"Błąd portu szeregowego: {e}")
    return None
