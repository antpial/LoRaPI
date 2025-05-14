import loralib         
import time  

loralib.init(0, 434000000, 7)  

while True:
    loralib.send(b'hello')
    time.sleep(1)