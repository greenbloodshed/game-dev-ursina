#====================================================================================================
# Greenbloodshed's first 'game' using Ursina Game Engine
# Reference/guide: https://www.ursinaengine.org/introduction_tutorial.html
#====================================================================================================

# All you can do is move left and right.

from ursina import * # Imports all necessary things from the engine

# create a window
app = Ursina()

# the first parameter tells us the Entity's model will be a 3d-model called 'cube'.
# ursina includes some basic models like 'cube', 'sphere' and 'quad'.
# the next parameter tells us the model's color should be orange.
# 'scale_y=2' tells us how big the entity should be in the vertical axis, how tall it should be.
# in ursina, positive x is right, positive y is up, and positive z is forward.
player = Entity(model='cube', color=color.orange, scale_y=2)

# create a function called 'update'.
# this will automatically get called by the engine every frame.

def update():
    player.x += held_keys['d'] * time.dt
    player.x -= held_keys['a'] * time.dt

# this part will make the player move left or right based on our input.
# to check which keys are held down, we can check the held_keys dictionary.
# 0 means not pressed and 1 means pressed.
# time.dt is simply the time since the last frame. by multiplying with this, the
# player will move at the same speed regardless of how fast the game runs.

def input(key):
    if key == 'space':
        player.y += 1
        invoke(setattr, player, 'y', player.y-1, delay=.25)

# start running the game
app.run()