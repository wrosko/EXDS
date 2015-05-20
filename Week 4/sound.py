# This library is a modified extract from PyGraphics developed at the
#University of Toronto
# Aug 2010: fixed envelope for stereo sounds; further restructuring
# May 2011: module is only one file now
# April 2015: remove pygame dependency, simplify code base

'''
The Sound and Sample classes. This currently supports only uncompressed
.wav files. For best quality use .wav files with sampling rates of either
22050 or 44100.
'''

import wave
import struct
from copy import deepcopy

import numpy as np

####################------------------------------------------------------------
## Sound class
####################------------------------------------------------------------

class Sound(object):
    '''A Sound class for representing wave files as arrays.'''
        
    def __init__(self, filename=None, samples=None, seconds=None,
            sample_rate=44100, channels=2):
        '''Create a Sound object.
                
        Arguments:
        filename -- str, filename with .wav extension (default None)
        samples -- int, number of samples for a blank sound (default None)
        seconds -- int, number of seconds for a blank sound (default None)
        sample_rate -- int, samples per second for the wave file (default 44100)
        channels -- int, number of channels, stereo=2, mono=1 (default 2)
        
        If a filename is give, that file will be opened and loaded into the
        resulting object, and samples and seconds will be ignored.  Otherwise,
        if samples or seconds is given a blank Sound instance will be created
        that has the given number of samples or a the given time length in
        seconds. The number of samples takes precedence of the number of
        seconds.  '''
        # Don't change the number of channels, I did this because I only want
        # to have StereoSounds for this lab.
        assert channels == 2
        self.channels = channels
        self.sample_rate = sample_rate
        
        if filename != None:
            self.filename = filename
            self._load_sound(filename)
            
        elif samples != None:
            self._create_sound(samples)
            
        elif seconds != None:
            samples = int(seconds * self.sample_rate)
            self._create_sound(samples)
            
        else:
            raise TypeError("No arguments were given to the Sound constructor.")
            
    def __eq__(self, snd):
        '''Equality testing semantics.
        
        Arguments:
        snd -- Another Sound object instance for comparison.
        
        This function gets called with the following operation `Sound == snd`.'''
        if self.channels == snd.channels:
            return np.all(self.samples == snd.samples)
        else:
            raise ValueError('Both sounds must have same number of channels.')
        
    def __str__(self):
        '''Return the number of Samples in this Sound as a str.
        
        This gets called with the following function call: `str(Sound)`.'''
        return "Sound of length " + str(len(self))


    def __iter__(self):
        '''Iterate through this Sound's samples from start to finish.
        
        This function gets called when the sound is used in a "for" loop. For
        example: 
        
            for sample in snd:
                #do something with sample
                
        Notice that it returns an instance of a StereoSample class, which is
        defined below.'''
        for i in range(len(self)):
            yield StereoSample(self.samples, i)

    def __len__(self):
        '''Return the number of Samples in this Sound.

        This gets called with the following function call: `len(Sound)`.'''
        return len(self.samples)

    def _load_sound(self, fname):
        '''Load a wavefile into the instance as a Numpy array.
        
        The leading underscore (_) indicates that this should be treated as a
        "private" function, and you shouldn't use this directly.  '''
        wavefile = wave.open(fname, 'r')
        params = wavefile.getparams()
        (nchannels, sampwidth, framerate, nframes, comptype, compname) = \
                params

        # Frames is a byte object. Must unpack this to a list of integers
        frames = wavefile.readframes(nframes*nchannels)
        out = struct.unpack("{:d}h".format(nframes*nchannels), frames)
        wavefile.close()

        # Convert this to a (n, number channels) Numpy array.
        samples = np.array(out, dtype=np.int16)
        samples = samples.reshape(-1, nchannels)

        self.samples = samples
        self._params = params
        self.channels = nchannels
        self.sample_rate = framerate

    def _create_sound(self, samples):
        '''Create a blank sound array.

        The leading underscore (_) indicates that this should be treated as a
        "private" function, and you shouldn't use this directly.  '''
        self.samples = np.zeros((samples, self.channels), dtype=np.int16)

    def get_sample(self, i):
        '''Return this Sound's Sample object at index i. 
        
        Arguments:
        i -- int, the index number of sounds sample.
        
        Negative indices are supported. The StereoSample Class is defined
        below.'''
        return StereoSample(self.samples, i)
    
    def get_max(self):
        '''Return this Sound's most positive sample value. 
        
        If this Sound is stereo, return the most positive value for both
        channels.'''
        return self.samples.max()
        
    def get_min(self):
        '''Return this Sound's most negative sample value. 
        
        If this Sound is stereo, return the most negative for both channels.'''
        return self.samples.min()

    def normalize(self):
        '''Maximize the amplitude of the Sound's wave. 
        
        This function will find the largest absolute valued sample and create
        a normalizing scaling factor. That scaling factor is applied to all
        samples in the sound. After scaling the largest absolute valued sample
        should be equal to the maximum allowed intensity. This can have the
        effect of increasing the volume of the Sound.'''
        maximum = np.abs(self.samples).max()
        # The maximum of a 16-bit signed integer is 32767
        factor = 32767.0/maximum        
        self.samples *= factor      
    
    def copy(self):
        '''Return a copy of this Sound.'''
        return deepcopy(self)

    def save_as(self, filename):
        '''Save this Sound to a new wave file.
        
        Arguments:
        filename -- str, Name of the new file to create. Don't forget the
        ".wav" extension.'''
        
        data = self.samples.ravel()
        wavefile = wave.open(filename, 'w')
        wavefile.setnchannels(self.channels)
        # This is from the previous iteration of this program, might be useful
        # later
#        # calculate the number of bytes for this sound
#        fmtbytes = (abs(self.encoding) & 0xff) >> 3
#        wav.setsampwidth(fmtbytes)
        # For a 2-bytes for a int16
        wavefile.setsampwidth(2)
        wavefile.setframerate(self.sample_rate)
        wavefile.setnframes(len(self))
        sample_bytes = struct.pack('h'*data.size, *data)
        wavefile.writeframes(sample_bytes)
        wavefile.close()

####################------------------------------------------------------------
## Sample Classes
####################------------------------------------------------------------

class StereoSample(object):
    '''A two-channeled Sample with a left and a right value.
    
    Attributes:
    samp_array -- Numpy array, the sound file data array
    i -- int, index number of this particular sample

    You should not need to create any StereoSample object instances by hand.
    Use methods of a Sound object instead. It will be good to look at the
    methods defined here, though, so you know what they do.
    '''
    def __init__(self, samp_array, i):
        # This next line doesn't do anything, but if i is out of bounds it
        # will throw an error
        samp_array[i]
        self.samp_array = samp_array
        self.index = i

    def get_index(self,):
        '''Return this samples index to the original Sound samples array.'''
        return self.index


    def __str__(self):
        '''Return a str with index and value information.

        This gets called with the following function call: `str(Sample)`.'''
        return "Sample at " + str(self.index) + " with left value " \
                 + str(self.get_left()) + " and right value " + \
                 str(self.get_right())
    
    def set_left(self, v):
        '''Set this Sample's left value.
        
        Arguments:
        v -- int, change the samples left value to this number'''
        
        if type(v) != int:
            raise TypeError("int expected")
        else:
            self.samp_array[self.index, 0] = v

    def set_right(self, v):
        '''Set this Sample's right value.

        Arguments:
        v -- int, change the samples left value to this number'''
        
        if type(v) != int:
            raise TypeError("int expected")
        else:
            self.samp_array[self.index, 1] = v
        
    def get_left(self):
        '''Return this Sample's left value.'''
        return self.samp_array[self.index, 0]
    
    def get_right(self):
        '''Return this Sample's right value.'''
        return self.samp_array[self.index, 1]

        
