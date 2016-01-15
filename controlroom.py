import mcpi.block as block
import time
import math
import random

class ControlRoom:
    def __init__(self, mc):
        self.mc = mc
        self.autojump = False
        self.worldImmutable = False
        self.nametags = True

        self.mc.setting("autojump", self.autojump)
        self.mc.setting("world_immutable", self.worldImmutable)
        self.mc.setting("nametags_visible", self.nametags)

    def toggleAutoJump(self):
        self.autojump = not self.autojump
        self.mc.setting("autojump", self.autojump)
        return(self.autojump)
    
    def toggleWorldImmutable(self):
        self.worldImmutable = not self.worldImmutable
        self.mc.setting("world_immutable", self.worldImmutable)
        return(self.worldImmutable)

    def toggleNametags(self):
        self.nametags = not self.nametags
        self.mc.setting("nametags_visible", False)
        return(self.nametags)
        
    def tree(self, x, y, z, wood = block.LEAVES.id, leaves = block.LEAVES.id):        
        self.mc.setBlocks(x,y,z, x,y+6,z, wood)
        self.mc.setBlocks(x+2,y+4,z+2, x-2,y+5,z-2, leaves)
        
        self.mc.setBlocks(x+3,y+4,z-1, x,y+5,z+1, leaves)
        self.mc.setBlocks(x-1,y+4,z+3, x+1,y+5,z, leaves)
        self.mc.setBlocks(x-3,y+4,z-1, x-3,y+5,z+1, leaves)
        self.mc.setBlocks(x-1,y+4,z-3, x+1,y+5,z, leaves)

        self.mc.setBlocks(x+1,y+6,z+1, x+2,y+6,z-1, leaves)
        self.mc.setBlocks(x-1,y+6,z+1, x-2,y+6,z-1, leaves)
        self.mc.setBlocks(x+1,y+6,z-1, x-1,y+6,z-2, leaves)
        self.mc.setBlocks(x+1,y+6,z+1, x-1,y+6,z+2, leaves)

        self.mc.setBlock(x,y+7,z, leaves)
        self.mc.setBlock(x+1,y+7,z, leaves)
        self.mc.setBlock(x-1,y+7,z, leaves)
        self.mc.setBlock(x,y+7,z+1, leaves)
        self.mc.setBlock(x,y+7,z-1, leaves)

        self.mc.setBlock(x,y+8,z, leaves)

    def waterWall(self, x, y, z, length = 2):
        self.mc.setBlocks(x - (length/2), y, z, x, y, z + (length/2), block.WATER_FLOWING.id)

    def groundLevel(self, x, z):
        y = -5 # 5 below sea level
        ground = False
        while not ground:
            y+=1
            b = self.mc.getBlock(x, y, z)
            if (b == block.AIR.id or b == block.SNOW.id): # if the block we've selected is air
                if (b == block.SNOW.id): self.mc.setBlock(x, y - 1, z, block.AIR.id)
                ground = True # we're at ground level
        return(y) # return the current y value

    def distance(self, x1, y1, z1, x2, y2, z2, height = False):
        xd = x1 - x2
        zd = z1 - z2
        if (height):
            yd = y1 - y2        
            d = math.sqrt((xd*xd) + (yd*yd) + (zd*zd))
        else:
            d = math.sqrt((xd*xd) + (zd*zd))
        return(d)
    
    def randomCoordinates(self):
        x = random.randint(-128, 128)
        z = random.randint(-128, 128)
        y = self.groundLevel(x, z)
        return {"x": x,
                "y": y,
                "z": z
                }
    
    def chase(self, wood = block.WOOD.id, leaves = block.LEAVES.id, randomplayer = False, player = None, threat="tree"):
        start = time.time()
        if randomplayer:
            player = random.choice(self.mc.getPlayerEntityIds())
        if not player:
            player = self.mc.getPlayerEntityIds()[0]
        pos = self.mc.entity.getPos(player)
        origin = self.randomCoordinates()
        if threat == "tree":
            self.tree(origin['x'], origin['y'], origin['z'], wood, leaves)
            increment = 5
        else:
            self.waterWall(origin['x'], origin['y'], origin['z'], length = 5)
            increment = 1

        distance = self.distance(pos.x, pos.y, pos.z, origin['x'], origin['y'], origin['z'])
        currentX = origin['x']
        currentZ = origin['z']
        while distance > 5:
            if (currentX < pos.x): currentX += increment
            if (currentX > pos.x): currentX -= increment
            if (currentZ < pos.z): currentZ += increment
            if (currentZ > pos.z): currentZ -= increment
            pos = self.mc.entity.getPos(player)
            currentY = self.groundLevel(currentX, currentZ)
            distance = self.distance(pos.x, pos.y, pos.z, currentX, currentY, currentZ)
            print(distance)
            if (self.mc.getBlock(currentX, currentY-1, currentZ) != leaves):
                if threat == "tree":
                    self.tree(currentX, currentY, currentZ, wood, leaves)
                else:
                    self.waterWall(currentX, currentY+5, currentZ, length = 5)
            time.sleep(0.5)
        duration = time.time() - start
        return(duration)
            
    def console(self):
        command = raw_input("> ")
        while command != "Q":
            if (command == "chase"):
               self.chase(block.OBSIDIAN.id, block.GLOWING_OBSIDIAN.ID)
            if (command == "ls"):
                for entityId in self.mc.getPlayerEntityIds():
                    print entityId
            if (command == "autojump"):
                 print("Auto jump is now " + ("enabled" if self.toggleAutoJump() else "disabled"))
            if (command == "immutable"):
                print("World is now " + ("immutable" if self.toggleWorldImmutable() else "mutable"))
            if (command == "nametags"):
                print("Nametags are now " + ("visible" if self.toggleNametags() else "invisble"))
            command = raw_input("> ")
