import sound

def rem_vocals(snd):
    for sample in snd:
        left = sample.get_left()
        right = sample.get_right()
        average = int((left - right)/2.0)
        sample.set_right(average)
        sample.set_left(average)
    return snd

def fade_in(snd, fade_length):
    for sample in snd:
        if sample.get_index() <= fade_length:
            left = sample.get_left()
            right = sample.get_right()
            
            
