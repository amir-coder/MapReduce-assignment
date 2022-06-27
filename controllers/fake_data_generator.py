

from random import randint, random, choice
import string

class FakeDataGenerator:
    

    def generate():
        files = []
        files.append(open('./tmp/doc1', 'ab')) 
        files.append(open('./tmp/doc2', 'ab')) 
        files.append(open('./tmp/doc3', 'ab')) 
        line = ""
        #define rand number of lines between 100 and 200
        nblines = randint(9999, 9999999)
        #define rand number of hosts
        nbhosts = randint(5, 15)
        #generate random host strings
        hosts = [(''.join(choice(string.ascii_letters) for _ in range(10))) for i in range(nbhosts)]
        tlds = ['com', 'net', 'dz']
        for _ in range(nblines):
            url = "https://" + hosts[randint(0, len(hosts) - 1)] + "." + tlds[randint(0, len(tlds) - 1)]
            size = str(randint(0 , 99999999))
            date = "not-important-data"
            line = ', '.join([url, size, date, '\n'])
            files[randint(0, 2)].write(bytes(line, 'utf-8'))
        #append to the file format url, size, date
