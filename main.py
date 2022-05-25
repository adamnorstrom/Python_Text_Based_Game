from random import randint
# establishing the character's class

player_name =  input("What's your name? \n")
Start= input("Type move to enter the Jungle Ahead {}.\n".format(player_name))
class Character:
# basically the constructor. To be noted is that def is used for creating functions and self. is used instead of this dot
  def __init__(self, tempName, tempHP, tempDie,):
    self.name = tempName
    self.hp = tempHP
    self.attackDie = tempDie
    
#making a different kind of attach function
  def spell(self,other):
     print('')
     print(self.name + ' uses a spell on ' + other.name)
     damage = randint(1,2*self.attackDie)
     print('{} did {} damage to {}.'.format(self.name, damage, other.name))
    # says that if the goblin or player is still alive then print how much hp it has 
     if other.hp >0:
      other.hp -= damage
      print(other.name +' has ' + str(other.hp) + ' hitpoints remaining.')
      # if the hp for either character is zero or below then the player or goblin is dead and the game will then print that
     else:
      print('{} is dead.'.format(other.name))

     print('')
# creates  function for attacking with self and other being filled by goblin and player 
  def attack(self, other):
    print('')
    print(self.name + ' attacking ' + other.name)
    damage = randint(1,self.attackDie)
    print('{} did {} damage to {}.'.format(self.name, damage, other.name))
    # says that if the goblin or player is still alive then print how much hp it has 
    if other.hp >0:
      other.hp -= damage
      print(other.name +' has ' + str(other.hp) + ' hitpoints remaining.')
      # if the hp for either character is zero or below then the player or goblin is dead and the game will then print that
    else:
    
       print('{} is dead.'.format(other.name))
    print('')

  def heal(self,other):
  #  Players ability to regain HP is limited by the heals number
   Heals = 9
  #  chooses a random number of hitpoints and adds to characters
   heal = randint(0,Heals)
   self.hp += heal
   other.hp += randint(0,Heals)
  #  prints how many hit points each character has left now that they both healed
   print(self.name + ' has '+ str(self.hp) + ' hitpoints remaining')
   print(other.name + '  has ' +str(other.hp) + ' hitpoints remaining\n')  
# these lines are creating new objects of the class Character with the inputs being for their names, their HP, and the upper bound for how much damage each player could possibly do in a turn
player = Character(player_name,20,6)
enemy = Character('Goblin',28,4)

if Start == 'move' :
  state=1
while state==1:  
  spells = input ("Type s to use a spell, a to attack normally, or use h to heal\n") 
  
  
  if spells[0] == 'a' :                   
     enemy.attack(player)
     player.attack(enemy)
  # this is how using the s control uses a spell
  if spells [0]== 's':
     enemy.spell(player)
     player.spell(enemy)
# if player chooses to use his healing by pressing h then this is activated
  if spells[0]== 'h':
    enemy.heal(player)
    player.heal(enemy)  

    # adds the rsult for winning
  if enemy.hp<= 0:
    print('goblin is dead. You won!')
    break
    # adds the result for losing
  if player.hp<=0:
    print('you are dead, game over')
    break
