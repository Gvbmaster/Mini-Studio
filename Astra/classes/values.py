class Param:
    gameName = "Astra"
    gameVersion = "v0.0"
    screenWidth = 1280
    screenHeight = 720
    soundVolume = 100
    musicVolume = 100
    fxVolume = 100

class PlayerStats:
    currentHealth = 2
    maxHealth = 3
    speed = 10
    #maxSpeed = 10
    attackDamage = 3
    #maxAttackDamage = 6
    attackSpeed = 1
    MaxAttackSpeed = 2
    isPlayerHitable = True
    

class EnnemieStats:
    currentHealth = 6
    maxHealth = 10
    speed = 7
    maxSpeed = 14
    attackDamage = 1
    maxAttackDamage = 2
    attackSpeed = 1
    MaxAttackSpeed = 2


class BossStats:
    currentHealth = 500
    maxHealth = 500
    speed = None
    maxSpeed = None
    attackDamage = 1
    maxAttackDamage = 2
    attackSpeed = 1
    MaxAttackSpeed = 2

class ObstacleStats:
    speed = 7
    #maxSpeed = 14

