import mcpi.minecraft as minecraft
import mcpi.block as block
from controlroom import ControlRoom
import time

mc = minecraft.Minecraft.create()
cr = ControlRoom(mc)

# Hunger Games-like tree chase (try changing the threat to "lava" or "water"
#mc.postToChat("We're hunting one of you down...")
#duration = cr.chase(block.OBSIDIAN.id, block.GLOWING_OBSIDIAN.id, randomplayer=True, threat="trees")
#print("You lasted %i seconds!" % duration)
#mc.postToChat("You lasted %i seconds!" % duration)

# This is Queen Elsa running across water
#while True:
#    pos = mc.player.getPos()
#    b = mc.getBlock(pos.x, pos.y-1, pos.z)
#    if (b == block.WATER.id or b == block.WATER_STATIONARY.id):
#        mc.setBlocks(pos.x-1, pos.y-1, pos.z-1, pos.x+1, pos.y-1, pos.z+1, block.ICE.id)

# fly player around in a circle at circle origin (0,0), height 20 and radius 50
#circlePath = cr.circlePath(0, 20, 0, 50)
#mc.camera.setFollow(mc.getPlayerEntityIds()[0])
#while True:
#	for coords in circlePath['coords']:
#		mc.player.setPos(coords)
#		time.sleep(0.025)
