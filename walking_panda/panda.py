from math import pi, sin, cos

from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor


class WalkingPanda(ShowBase):

    def __init__(self, no_rotate=False, anti_clockwise=False, scale=1, size=0.005):
        ShowBase.__init__(self)

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
            base.trackball.node().setPos(0, 20, -3)

        # Load and transform the panda actor.
        self.pandaActor = Actor("models/panda-model",
                                {"walk": "models/panda-walk4"})
        self.pandaActor.setScale(size*scale, size*scale, size*scale)
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
        self.camera.setPos(20 * sin(angleRadians), -20.0 * cos(angleRadians), 3)
        self.camera.setHpr(angleDegrees, 0, 0)
        return Task.cont


# walking = WalkingPanda()
# walking.run()