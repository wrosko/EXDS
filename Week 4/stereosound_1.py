import sound

def rem_vocals(snd):
    sndcopy = snd.copy()
    for sample in sndcopy:
        left = sample.get_left()
        right = sample.get_right()
        average = int((left - right)/2.0)
        sample.set_right(average)
        sample.set_left(average)
    return sndcopy

def fade_in(snd, fade_length):
    sndcopy = snd.copy()
    for sample in sndcopy:
        if sample.get_index() <= (fade_length-1):
            right = sample.get_right()
            left = sample.get_left()
            newleft = int((sample.get_index() / fade_length)* left)
            newright = int((sample.get_index() / fade_length)* right)
            sample.set_right(newright)
            sample.set_left(newleft)

    return sndcopy

def fade_out(snd, fade_length):
    sndcopy = snd.copy()
    start_fade = len(sndcopy) - (fade_length)
    n = fade_length
    for sample in sndcopy:
        if sample.get_index() >= start_fade:
            right = sample.get_right()
            left = sample.get_left()
            newleft = int(( n / fade_length)* left)
            newright = int(( n / fade_length)* right)
            n -= 1
            sample.set_right(newright)
            sample.set_left(newleft)

    return sndcopy
