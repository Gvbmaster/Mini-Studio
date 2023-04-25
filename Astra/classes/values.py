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
    attackSpeed = 100 # cadence de tir
    MaxAttackSpeed = 2
    attackVelocity = 20 #speed bullet
    shield = False
    isPlayerHitable = True

class EnnemieStats:
    currentHealth = 6
    maxHealth = 10
    speed = 2
    maxSpeed = 14
    attackDamage = 1
    maxAttackDamage = 2
    attackSpeed = 1
    maxAttackSpeed = 2
    pattern1=[(1250,350),(1500,100),(1750,350),(1500,600)]
    meanP1=(int((pattern1[0][0]+pattern1[1][0]+pattern1[2][0]+pattern1[3][0])/4),int((pattern1[0][1]+pattern1[1][1]+pattern1[2][1]+pattern1[3][1])/4))
    pattern2=[(1500,100),(1750,350),(1500,600),(1250,350)]
    meanP2=(int((pattern2[0][0]+pattern2[1][0]+pattern2[2][0]+pattern2[3][0])/4),int((pattern2[0][1]+pattern2[1][1]+pattern2[2][1]+pattern2[3][1])/4))
    pattern3=[(1720,100),(1720,541),(1520,540),(1520,981)]
    pattern4=[(1720,100),(1500,320),(1720,541),(1500,761)]
    
    patternSpawn=[pattern1,pattern2,pattern3,pattern4]
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