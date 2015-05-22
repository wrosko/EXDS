'''
File: Kalra_Rosko_stereosound.py
Authors: Kalra, Rosko
Description: A sound modification program that uses a sound module that
    contains two custom classes for working with .wav sound files. The
    first function removes vocals from a music sound file, the second
    adds a fade-in to the sound, the third adds a fade-out, and the
    last adds both a fade-in and a fade-out
'''


import sound

def rem_vocals(snd):
    """
    rem_vocals() takes a sound object that has vocals, creates a copy, strips
    the vocals from the copy, and then returns the copy with no vocals.
    """
    
    sndcopy = snd.copy()#create a copy of the sound
    #Call an iterating loop that looks at each sample in the sndcopy
    #and stores the value for the left and right side of the sndcopy.
    #It takes the left and subtracts the right, then divides by two. This new
    #value is then stored as the left and right value. 
    for sample in sndcopy:
        left = sample.get_left()
        right = sample.get_right()
        newvalue = int((left - right)/2.0)
        sample.set_right(newvalue)
        sample.set_left(newvalue)
    return sndcopy #Return the modified sndcopy

def fade_in(snd, fade_length):
    """
    fade_in() takes a snd and the fade_length. It creates a copy of snd,
    modifies the snd copy by making the volume of the sound linearly increase
    from 0 over the given number of samples, and then returns the modified
    copy.
    """
    
    sndcopy = snd.copy()#create a copy of the sound
    #Run an iterating loop that looks at each sample in the sndcopy
    #and stores the value for the left and right side of the sndcopy.
    
    for sample in sndcopy:
        #As long as the sample's index is less than the fade length, the
        #sample will be modified accordingly
        if sample.get_index() < (fade_length):
            
            right = sample.get_right()
            left = sample.get_left()
            #newleft and newright are assigned a value that is a fraction
            #of the original value. The fraction approaches the value 1.0
            #after each iteration.
            newleft = int((float(sample.get_index()) / fade_length) * left)
            newright = int((float(sample.get_index()) / fade_length) * right)
            sample.set_right(newright)
            sample.set_left(newleft)
            
    return sndcopy

def fade_out(snd, fade_length):
    """
    fade_out() takes a snd and the fade_length. It creates a copy of snd, then
    modifies the snd copy by making the volume of the sound linearly decrease
    to 0. The decrease starts to happen at fade_length samples from the end of
    the sound. The modified copy is returned.
    """
    sndcopy = snd.copy()#create a copy of the sound
    start_fade = len(sndcopy) - (fade_length)#establish value where the fade
                                             #will start.
    n = float(fade_length - 1)#takes fade_length and shifts the value so it
                              #starts at 0.
    for sample in sndcopy:
        #As long as the sample's index is greater than or equal to the start 
        #fade position, the sample will be modified accordingly.
        if sample.get_index() >= start_fade:
            right = sample.get_right()
            left = sample.get_left()
            #newleft and newright are assigned a value that is a fraction
            #of the original value. The fraction goes to 0 after each
            #iteration. 
            newleft = int(( n / fade_length) * left)
            newright = int(( n / fade_length) * right)
            n -= 1.0 #subtract 1.0 after each iteration to make the above
                     #variables go to 0.
            sample.set_right(newright)
            sample.set_left(newleft)

    return sndcopy 

def fade(snd, fade_length):
    """
    fade() creates a copy of snd, and then calls on the functions fade_in()
    and fade_out(). The sound copy is set equal to the returned sound from the
    fade_in() and fade_out() functions. 
    """
    
    sndcopy = snd.copy()#creates a snd copy
    
    #store the returned value from the fade_in and fade_out functions
    #as sndcopy. This makes it so that sndcopy will end up containing the
    #modification from fade_in and fade_out.
    sndcopy = fade_in(sndcopy, fade_length)
    sndcopy = fade_out(sndcopy, fade_length)#sndcopy contains the fade_in,
                                            #fade_out is added here.
    return sndcopy
    
    





