from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from math import pi, sin, cos
from playsound import playsound

class WalkingPanda(ShowBase):

    def __init__(self, no_rotate=False, reverse=False,
                 no_walk=False, scale=1, location=[-8, 42]):
        ShowBase.__init__(self)
        playsound("forest.mp3", False)
        # Load the environment model.
        self.scene = self.loader.loadModel("models/environment")
        # Reparent the model to render.
        self.scene.reparentTo(self.render)
        # Apply scale and position transforms on the model.
        self.scene.setScale(0.25, 0.25, 0.25)
        if location:
            self.scene.setPos(location[0], location[1], 0)
        else:
            self.scene.setPos(-8, 42, 0)
        # Add the spinCameraTask procedure to the task manager.
        self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")

        # Load and transform the panda actor.
        self.pandaActor = Actor("models/panda-model",
                                {"walk": "models/panda-walk4"})
        self.pandaActor.setScale(0.005, 0.005, 0.005)
        if scale:
            self.pandaActor.setScale(0.005 * scale, 0.005 * scale, 0.005 * scale)
        self.pandaActor.reparentTo(self.render)
        # Loop its animation.
        if not no_walk:
            self.pandaActor.loop("walk")
        self.no_rotate = no_rotate
        self.reverse = reverse
        self.no_rotate = no_rotate

    # Define a procedure to move the camera.
    def spinCameraTask(self, task):
        if self.no_rotate:
            angleDegrees = 0
        else:
            if self.reverse:
                angleDegrees = task.time * -6.0
            else:
                angleDegrees = task.time * 6.0
        angleRadians = angleDegrees * (pi / 180.0)
        self.camera.setPos(20 * sin(angleRadians), -20.0 * cos(angleRadians), 3)
        self.camera.setHpr(angleDegrees, 0, 0)
        return Task.cont
