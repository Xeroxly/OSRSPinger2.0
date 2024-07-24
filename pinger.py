import subprocess
import threading
import os

if(os.path.exists('results.txt')):
    os.remove('results.txt')

# List of OSRS Worlds to be checked (Currently USA West Coast P2P Worlds)
# 6 = OSRS World 306, 120 = OSRS World 420, etc..
worldList = ["6", "7", "13", "15", "19", "20", "23", "24", "31", "32", "38", "39", "40", "47", "48", 
             "55", "56", "57", "74", "78", "120", "121", "122", "129", "141", "143", "144", "145", "146"]

f = open('results.txt', 'a')

def world2Command(world):
    return 'PING oldschool' + world + '.runescape.com'

# Map world numbers to executable commands
commandList = list(map(world2Command, worldList))

# Define what each thread should do
def singleWorldPing(command):
    result = subprocess.check_output(command, shell=True, text=True)
    output = worldList[commandList.index(command)] + ' | ' + result[-5:]
    f.write(output)

# Open a new thread for every world to be pinged
for command in commandList:
    x = threading.Thread(target=singleWorldPing, args=(command,))
    x.start()
