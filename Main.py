from Game import Game
import time
import Player

# here is where we determine what happens in the game
game = Game()
player = Player.Teymur()

time.sleep(1)
enemy = game.encounterEnemy(1, 10, "Goblin")
Game.listenForAttack(player, enemy)
