import mcpi.minecraft as minecraft
import mcpi.block as block
from controlroom import ControlRoom

mc = minecraft.Minecraft.create()
cr = ControlRoom(mc)

mc.postToChat("We're hunting one of you down...")
duration = cr.chase(block.OBSIDIAN.id, block.GLOWING_OBSIDIAN.id, randomplayer=True, threat="lava")
print("You lasted %i seconds!" % duration)
mc.postToChat("You lasted %i seconds!" % duration)
