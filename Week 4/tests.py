import unittest
from sound import Sound
import ??? as myfile
# ??? should be replaced with the name of
#the file which has your functions.

def three_samples():
      '''Return a new sound with three samples.'''
      snd = Sound(samples=3)
      smp = snd.get_sample(0)
      smp.set_left(1010)
      smp.set_right(80)
      smp = snd.get_sample(1)
      smp.set_left(1500)
      smp.set_right(-4200)
      smp = snd.get_sample(2)
      smp.set_left(-65)
      smp.set_right(28132)
      return snd

def three_samples_rem_vocals():
      '''Return a new sound to which vocal-removal has been applied.'''
      snd = Sound(samples=3)
      smp = snd.get_sample(0)
      smp.set_left(465)
      smp.set_right(465)
      smp = snd.get_sample(1)
      smp.set_left(2850)
      smp.set_right(2850)
      smp = snd.get_sample(2)
      smp.set_left(-14098)
      smp.set_right(-14098)
      return snd

def four_samples():
      '''Return a new sound with four samples.'''
      snd = Sound(samples=4)
      smp = snd.get_sample(0)
      smp.set_left(1008)
      smp.set_right(80)
      smp = snd.get_sample(1)
      smp.set_left(1500)
      smp.set_right(-4200)
      smp = snd.get_sample(2)
      smp.set_left(64)
      smp.set_right(28132)
      smp = snd.get_sample(3)
      smp.set_left(148)
      smp.set_right(148)
      return snd

def four_samples_fade_in():
      '''Return a new sound to which a fade-in has been applied over the
      entire sound.'''
      snd = Sound(samples=4)
      smp = snd.get_sample(0)
      smp.set_left(0)
      smp.set_right(0)
      smp = snd.get_sample(1)
      smp.set_left(375)
      smp.set_right(-1050)
      smp = snd.get_sample(2)
      smp.set_left(32)
      smp.set_right(14066)
      smp = snd.get_sample(3)
      smp.set_left(111)
      smp.set_right(111)
      return snd

def four_samples_fade_out():
      '''Return a new sound to which fade-out has been applied.'''
      snd = Sound(samples=4)
      smp = snd.get_sample(0)
      smp.set_left(756)
      smp.set_right(60)
      smp = snd.get_sample(1)
      smp.set_left(750)
      smp.set_right(-2100)
      smp = snd.get_sample(2)
      smp.set_left(16)
      smp.set_right(7033)
      smp = snd.get_sample(3)
      smp.set_left(0)
      smp.set_right(0)
      return snd

def four_samples_fade():
      '''Return a new sound to which fade has been applied.'''
      snd = Sound(samples=4)
      smp = snd.get_sample(0)
      smp.set_left(0)
      smp.set_right(0)
      smp = snd.get_sample(1)
      smp.set_left(187)
      smp.set_right(-525)
      smp = snd.get_sample(2)
      smp.set_left(8)
      smp.set_right(3516)
      smp = snd.get_sample(3)
      smp.set_left(0)
      smp.set_right(0)
      return snd

class TestCases(unittest.TestCase):
    def setUp(self):
        pass
  
    def test_rem_vocals(self):
        '''Test rem_vocals.'''
        snd = three_samples()
        sol = three_samples_rem_vocals()
        studentsol = myfile.rem_vocals(snd)
        self.assertEqual(studentsol, sol)    
        self.assertNotEqual(studentsol, snd)

if __name__ == '__main__':
  unittest.main()
