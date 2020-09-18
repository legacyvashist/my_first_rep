class song :
 def __init__(self,lyric):
  self.lyric = lyric
 def singing(self):
   for i in self.lyric:
           print(i)

bday_song = song("happy birthday to you my dear")
bday_song.singing()