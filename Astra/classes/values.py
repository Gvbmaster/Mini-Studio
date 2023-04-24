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
    attackSpeed = 100
    MaxAttackSpeed = 2   
    

class EnnemieStats:
    currentHealth = 6
    maxHealth = 10
    speed = 5
    maxSpeed = 14
    attackDamage = 1
    maxAttackDamage = 2
    attackSpeed = 1
    maxAttackSpeed = 2
    pattern1=[(1000,350),(750,600),(500,350),(750,100)]
    pattern2=[(1000,350),(750,600),(500,350),(750,100)]
    patternSpawn=[pattern1,pattern2]
    killCount=0
    enemyAlive=0
    pattern=0
    type=None


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

