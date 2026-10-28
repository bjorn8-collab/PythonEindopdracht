player_class = "Warrior"

health = 0
damage = 0
bekende_class = True


match player_class:
    case "Warrior":
        health = 150
        damage = 20
    case "Mage":
        health = 80
        damage = 35
    case "Archer":
        health = 100
        damage = 25
    case "Rogue":
        health = 90
        damage = 30
        
if bekende_class:
    print(f" Je hebt gekozen voor: {player_class}")
    print(f" Health: {health}")
    print(f" Damage: {damage}")
        
