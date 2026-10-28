monster_health = 150
player_damage = 25
aantalAanvallen = 0

while monster_health > 0:
    monster_health = monster_health - player_damage
    aantalAanvallen = aantalAanvallen + 1
    
    if monster_health <0:   
        monster_health = 0
    
    
    print(f"je valt aan en doet {player_damage} damage. Het monster heeft nog {monster_health} HP over.")
    
