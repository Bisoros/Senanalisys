from timeit import default_timer as timer
from senanalisys import Senanalisys as sa

sum = 0
nr = 100
for i in range(nr):
    start = timer()

    text = 'Ich liebe Katze'
    var = sa(text)

    end = timer()
    print (end - start)
    sum += (end - start)

print ('end:' + str(sum/nr))
