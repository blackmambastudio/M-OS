#!/usr/bin/env python
from .BaseScene import SceneBase

class GameScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
    
    def ProcessInput(self, events, pressed_keys):
        pass
        
    def Update(self, dt):
        pass
    
    def Render(self, screen):
        # The game scene is just a blank blue screen 
        screen.fill((0, 0, 255))