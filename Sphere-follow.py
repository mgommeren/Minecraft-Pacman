from mcpi.minecraft import Minecraft
from time import sleep

mc = Minecraft.create()

sleep(2)
mc.postToChat("Sphere")


radius = 5
OffSet = 8
OldPos = mc.player.getPos()


def BuildSphere(Pos):
    currentPos = Pos
    for x in range(radius*-1,radius):
        for y in range(radius*-1, radius):
            for z in range(radius*-1,radius):
                if x**2 +y**2 +z**2 < radius**2:
                    mc.setBlock(currentPos.x+x, currentPos.y +y + radius, currentPos.z -z -OffSet, 35,4)

def DeleteSphere(Pos):
    currentPos = Pos
    for x in range(radius*-1,radius):
        for y in range(radius*-1, radius):
            for z in range(radius*-1,radius):
                if x**2 +y**2 +z**2 < radius**2:
                    mc.setBlock(currentPos.x+x, currentPos.y +y + radius, currentPos.z -z -OffSet, 0)


while True:
    playerPos = mc.player.getPos()
    if OldPos.x / playerPos.x != 1 or OldPos.y / playerPos.y != 1 or OldPos.z / playerPos.z != 1:
        DeleteSphere(OldPos)
        BuildSphere(playerPos)
        OldPos = playerPos
