from map import Map
from character import *
from inventory import Inventory

game_map = Map(5, 5)

game_map.tiles[0][0] = 'S'
game_map.tiles[4][4] = 'E'
game_map.tiles[2][2] = 'I'
game_map.tiles[2][4] = 'V'

# Create a character and add an inventory
hero = hero("Peter", 100, 5)
sword = Inventory(name="Sword", damage=15)
villian = enemy("Oct", 15, 5)


while True:
    # Print the map with the current hero position
    game_map.print_map(hero.position)

    # Get user input for movement
    move = input("Enter direction (W/A/S/D): ").upper()

    # Update hero position based on input
    if move == 'W' and hero.position[0] > 0:
        hero.position = (hero.position[0] - 1, hero.position[1])
    elif move == 'A' and hero.position[1] > 0:
        hero.position = (hero.position[0], hero.position[1] - 1)
    elif move == 'S' and hero.position[0] < game_map.height - 1:
        hero.position = (hero.position[0] + 1, hero.position[1])
    elif move == 'D' and hero.position[1] < game_map.width - 1:
        hero.position = (hero.position[0], hero.position[1] + 1)

    # Check for end position
    if hero.position == game_map.end_position:
        print("You reached the end of the map! Game Over.")
        break

    # Check for special tiles and interact with inventory
    current_tile = game_map.tiles[hero.position[0]][hero.position[1]]
    if current_tile == 'S':
        print("You are on the start tile.")
    elif current_tile == 'E':
        print("You are on the end tile. You need to reach it to finish the game.")
    elif current_tile == 'I':
        print("You have a sowrd that does 15 damage.")
        hero.inventory = sword
    elif current_tile == 'V':
        print("You have encountered an enemy")
        print("You use your sowrd")
        hero.attack(villian)
        villian.attack(hero)       
    elif current_tile == 'O' and hero.inventory:
        hero.inventory.use()
    