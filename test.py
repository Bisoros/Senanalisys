from timeit import default_timer as timer
from senanalisys import Senanalisys as sa

sum = 0
nr = 100
for i in range(nr):
    start = timer()

    text = 'Wenn es dem internationalen Finanzjudentum in und außerhalb Europas gelingen sollte, die Völker noch einmal in einen Weltkrieg zu stürzen, dann wird das Ergebnis nicht der Sieg des Judentums sein, sondern die Vernichtung der jüdischen Rasse in Europa! '
    var = sa(text)

    end = timer()
    print (end - start)
    sum += (end - start)

print ('end:' + str(sum/nr))
