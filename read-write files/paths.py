import os
os.path.join('usr', 'bin', 'spam')
os.getcwd()
os.chdir('C:\\Windows\\System32')
os.makedirs('C:\\delicious\\walnut\\waffles')
os.path.abspath(path)
os.path.isabs(path) #will return True if the argument is an absolute path and False if it is a relative path
os.path.relpath(path, start) 

path = 'C:\\Windows\\System32\\calc.exe'
os.path.basename(path) #'calc.exe'
os.path.dirname(path) #'C:\\Windows\\System32'
os.path.split(calcFilePath) #('C:\\Windows\\System32', 'calc.exe')
calcFilePath.split(os.path.sep) #['C:', 'Windows', 'System32', 'calc.exe']
'/usr/bin'.split(os.path.sep) #['', 'usr', 'bin']

os.path.getsize('C:\\Windows\\System32\\calc.exe') #776192
os.listdir('C:\\Windows\\System32') #Calling os.listdir(path) will return a list of filename strings for each file in the path argument. (Note that this function is in the os module, not os.path.)

os.path.exists('C:\\some_made_up_folder') #False
os.path.isdir('C:\\Windows\\System32\\calc.exe') #False
os.path.isfile('C:\\Windows\\System32\\calc.exe') #True






