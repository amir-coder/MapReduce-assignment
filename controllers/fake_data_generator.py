

from random import randint, random, choice
import string

class FakeDataGenerator:
    

    def generate(path = './assets/corpus.txt'):
        with open(path, 'ab') as f:
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
                f.write(bytes(line, 'utf-8'))
            #append to the file format url, size, date
