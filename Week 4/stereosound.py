from sound import *

def rem_vocals(snd):
    for sample in snd:
        left = sample.get_left()
        right = sample.get_right()
        average = int((left - right)/2.0)
        #print sample.__str__()
        sample.set_right(average)
        sample.set_left(average)
        #print sample.__str__()
    return snd
