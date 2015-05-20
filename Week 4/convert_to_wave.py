import sound
import stereosound_1 as myfile
# ??? should be replaced with the name of
#the file which has your functions.

#Read the statements and comments below.
#You will need to make appropriate changes to the statements
#to work with different wav files and test various functions
#you have written.

#Converts the sound in grace.wav file to a Sound object.
snd = sound.Sound(filename='water.wav')

#The function fade that you have written is called
#and the Sound object it returns is assigned to gracefade.
waterfaded = myfile.fade_out(snd, 100000.0)

#The Sound object gracefade is converted to sound in
#a wav file called grace_fade.wav.
#This wav file did not exist before but is newly created.
waterfaded.save_as('waterfadeds.wav')



