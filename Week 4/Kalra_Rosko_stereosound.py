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
        if sample.get_index() < (fade_length):
            right = sample.get_right()
            left = sample.get_left()
            newleft = int((float(sample.get_index()) / fade_length) * left)
            newright = int((float(sample.get_index()) / fade_length) * right)
            sample.set_right(newright)
            sample.set_left(newleft)
    return sndcopy

def fade_out(snd, fade_length):
    sndcopy = snd.copy()
    start_fade = len(sndcopy) - (fade_length)
    n = float(fade_length - 1)
    print len(sndcopy)
    for sample in sndcopy:
        if sample.get_index() >= start_fade:
            right = sample.get_right()
            left = sample.get_left()
            newleft = int(( n / fade_length) * left)
            newright = int(( n / fade_length) * right)
            n -= 1.0
            sample.set_right(newright)
            sample.set_left(newleft)

    return sndcopy

def fade(snd, fade_length):
    sndcopy = snd.copy()
    sndcopy = fade_in(sndcopy, fade_length)
    sndcopy = fade_out(sndcopy, fade_length)
    return sndcopy
    
    





