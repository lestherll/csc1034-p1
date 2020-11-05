from math import pi, sin, cos

from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor


class WalkingPanda(ShowBase):

    def __init__(self, no_rotate=False, anti_clockwise=False, top_view=False, scale=1, size=0.005, no_panda=False,):
        ShowBase.__init__(self)

        # make parameters attribute so it can be accessed by instances
        self.no_rotate = no_rotate
        self.anti_clockwise = anti_clockwise
        self.top_view = top_view
        self.no_panda = no_panda

        # calculate actual size of the panda actor
        self.scale = scale
        self.size = size
        self.actual_size = self.scale * self.size

        # this attribute dictates which way the camera
        # will rotate if --no-rotate is False
        self.multiplier = -1 if anti_clockwise is True else 1

        # sound attributes
        self.loop_bg_sound = True
        self.bg_sound_vol = 0.5

        # MAIN SCENE
        # Load the environment model.
        self.scene = self.loader.loadModel("models/environment")
        # Reparent the model to render.
        self.scene.reparentTo(self.render)
        self.scene.setScale(0.25, 0.25, 0.25)   # scale scene
        self.scene.setPos(-8, 42, 0)    # set position of the scene

        # Set default view every time the program starts
        self.setDefaultView()

        # Check if --no-rotate param was passed
        if self.no_rotate is False:
            # Add the spinCameraTask procedure to the task manager.
            self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")

        # Override default view and set to top view if --top-view was passed
        if self.top_view is True:
            self.setTopView()

        # Load the panda actor.
        self.pandaActor = Actor("models/panda-model",
                                {"walk": "models/panda-walk4"})

        # check if --no-panda was passed
        if self.no_panda is False:
            self.setPanda()     # Render panda actor
            self.pandaActor.loop("walk")    # Loop walking animation.

        # play and loop sound
        self.backgroundMusic = self.loader.loadSfx("sound/Forest-ambience.mp3")
        self.backgroundMusic.setLoop(self.loop_bg_sound)
        self.backgroundMusic.play()
        self.backgroundMusic.setVolume(self.bg_sound_vol)

    # Define a procedure to move the camera.
    def spinCameraTask(self, task):
        angleDegrees = task.time * 6.0 * self.multiplier
        angleRadians = angleDegrees * (pi / 180.0)
        self.camera.setPos(20 * sin(angleRadians), -20.0 * cos(angleRadians), 3)
        self.camera.setHpr(angleDegrees, 0, 0)
        return Task.cont

    # Set camera orientation to default view
    def setDefaultView(self):
        # set position of camera without disabling mouse
        base.trackball.node().setPos(0, 20, -3)

    # Set camera orientation to top view
    def setTopView(self):
        base.trackball.node().setPos(0, 20, 0)
        base.trackball.node().setHpr(0, 90, 0)

    # Method to render panda
    def setPanda(self):
        # Scale panda using calculated size
        self.pandaActor.setScale(self.actual_size, self.actual_size, self.actual_size)
        self.pandaActor.reparentTo(self.render)

