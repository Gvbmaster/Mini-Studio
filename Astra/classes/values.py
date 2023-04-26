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
    attackDamage = 3
    attackSpeed = 20 # cadence de tir
    MaxAttackSpeed = 2
    attackVelocity = 10 #speed bullet
    shield = False
    isPlayerHitable = True

class EnnemieStats:
    currentHealth = 6
    maxHealth = 10
    speed = 2
    maxSpeed = 14
    attackDamage = 1
    maxAttackDamage = 2
    attackVelocity = 3 #speed bullet
    attackSpeed = 2000
    maxAttackSpeed = 2000
    pattern1=[(1250,250),(1500,0),(1750,250),(1500,500),(1250,760),(1500,510),(1750,760),(1500,1010)]
    pattern2=[(1500,0),(1750,250),(1500,500),(1250,250),(1500,510),(1750,760),(1500,1010),(1250,760)]
    pattern3=[(1720,100),(1720,541),(1520,540),(1520,981),(1320,100),(1320,541),(1120,540),(1120,981)]
    pattern4=[(1720,100),(1500,320),(1720,541),(1500,761),(1220,100),(1000,320),(1220,541),(1000,761)]
    patternSpawn=[pattern1,pattern2,pattern3,pattern4]
    killCount=0
    enemyAlive=0
    pattern=0
    
class fontCombo:
    oldCartoon=["img/combo old cartoon/x.png","img/combo old cartoon/1.png","img/combo old cartoon/2.png","img/combo old cartoon/3.png","img/combo old cartoon/4.png","img/combo old cartoon/5.png","img/combo old cartoon/6.png","img/combo old cartoon/7.png","img/combo old cartoon/8.png","img/combo old cartoon/9.png"]

# class EnergyBar:
#     def energy_bar(self):
#         energy=0


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
