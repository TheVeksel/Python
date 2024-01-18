import random

def lotto():
    numerot = random.sample(range(1, 41), 7)
    
    numerot.sort()
    
    lottonumerot = ",".join(map(str, numerot))
    
    return lottonumerot

lottorivi = lotto()
print(lottorivi)
