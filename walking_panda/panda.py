from math import pi, sin, cos

from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor


class WalkingPanda(ShowBase):

    def __init__(self, no_rotate=False, anti_clockwise=False, top_view=False, scale=1, size=0.005):
        ShowBase.__init__(self)

        # make parameters attribute so it can be accessed by instances
        self.no_rotate = no_rotate
        self.anti_clockwise = anti_clockwise

        # this attribute dictates which way the camera
        # will rotate if --no-rotate is False
        self.multiplier = -1 if anti_clockwise is True else 1

        # calculate actual size of the panda actor
        self.scale = scale
        self.size = size
        self.actualSize = self.scale * self.size

        # Load the environment model.
        self.scene = self.loader.loadModel("models/environment")
        # Reparent the model to render.
        self.scene.reparentTo(self.render)
        # Apply scale and position transforms on the model.
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-8, 42, 0)

        # Check if --no-rotate param was passed
        if no_rotate is False:
            # Add the spinCameraTask procedure to the task manager.
            self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")
        else:
            # Default view
            self.setDefaultView() if top_view is False else self.setTopView()

        # Load and transform the panda actor.
        self.pandaActor = Actor("models/panda-model",
                                {"walk": "models/panda-walk4"})
        self.pandaActor.setScale(self.actualSize, self.actualSize, self.actualSize)
        self.pandaActor.reparentTo(self.render)

        # Loop its animation.
        self.pandaActor.loop("walk")

        # play sound
        self.backgroundMusic = self.loader.loadSfx("sound/Great_Escape.mp3")
        self.backgroundMusic.play()
        self.backgroundMusic.setVolume(0.5)

    # Define a procedure to move the camera.
    def spinCameraTask(self, task):
        angleDegrees = task.time * 6.0
        angleRadians = angleDegrees * (pi / 180.0)
        self.camera.setPos(self.multiplier * 20 * sin(angleRadians), -20.0 * cos(angleRadians), 3)
        self.camera.setHpr(self.multiplier * angleDegrees, 0, 0)
        return Task.cont

    def setDefaultView(self):
        base.trackball.node().setPos(0, 20, -3)

    def setTopView(self):
        base.trackball.node().setPos(0, 20, 0)
        base.trackball.node().setHpr(0, 90, 0)