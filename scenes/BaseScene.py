#!/usr/bin/env python
import pytweening

from comm import comm
from utils import utils

class SceneBase:
    def __init__(self):
        self.next = self
        self.comm = comm
        self.time_triggers = []
        self.tweens = []
    
    def ProcessInput(self, events):
        print("uh-oh, you didn't override this in the child class")

    def Update(self, dt):
        self.CheckTriggers(dt)
        self.CheckTweens(dt)


    def Render(self, screen):
        print("uh-oh, you didn't override this in the child class")

    def SwitchToScene(self, next_scene):
        if next_scene == None:
            self.next = None
            return
        self.next = next_scene()

    def Terminate(self):
        self.SwitchToScene(None)

    def AddTrigger(self, timeout, obj, func, *params):
        self.time_triggers.append([timeout, obj, func, params])

    def CheckTriggers(self, dt):
        for trigger in self.time_triggers:
            trigger[0] -= dt
            if trigger[0] <= 0:
                getattr(trigger[1], trigger[2])(*trigger[3])
                self.time_triggers.remove(trigger)

    def AddTween(self, tween, timeout, obj, prop, start, end, delay=0):
        new_tween = utils.Tween(getattr(pytweening, tween), timeout, obj, prop, start, end, delay)
        self.tweens.append(new_tween)

    def CheckTweens(self, dt):
        for tween in self.tweens:
            tween.Update(dt)
            if tween.Finished():
                self.tweens.remove(tween)