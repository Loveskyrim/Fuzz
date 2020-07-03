import os

filename = 'bash.txt'
with open(os.getcwd()+'\\\\'+filename, 'r') as f, open(os.getcwd()+'\\\\min_'+filename, 'w') as d:
    for line in f:
        d.write(line.split()[0]+'\n')

