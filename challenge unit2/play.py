class player:
  def play(self):
    print("The player is playing cricket.")
#define the class batsman
class Batsman(player):
  def play(self):
    print("The batsman is batting.")
#define the class bowler
class Bowler(player):
  def play(self):
    print("The bowler is bowling.")
#create object
batsman=Batsman()
bowler=Bowler()
#call the play
batsman.play()
bowler.play()