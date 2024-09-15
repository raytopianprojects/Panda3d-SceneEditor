##########################################################################################################
# Auto Generated Code by Scene Editor
# Edit with caution
# Using this file in your code:
# For example, if you have named this file as "myscene.py"
# Do the following:
# from myscene import * 
# theScene=SavedScene() #instantiate the class
# IMPORTANT: All the documentation below refers to "theScene" as the instance of SavedScene()
##########################################################################################################

##########################################################################################################
# Import Panda Modules
##########################################################################################################
from direct.directbase.DirectStart import * # Core functionality for running the "show"
from direct.actor import Actor # Importing models with animations
from direct.directutil import Mopath # Motion Paths
from direct.interval import MopathInterval # Motion Paths
from direct.interval.IntervalGlobal import * # Intervals for interpolation, sequencing and parallelization
from direct.particles import ParticleEffect # Particle Systems
from direct.particles import ForceGroup # Forces acting on Particles
from direct.particles import Particles

##########################################################################################################
# This class stores the entire scene
##########################################################################################################

class SavedScene(DirectObject): # We inherit from DirectObject so that we can use self.accept method to catch messages

    # These dictionaries are required for re-loading a scene in the editor
    # They can be used to access the objects as well

    ModelDic={}# Stores all the models and static geometry
    ModelRefDic={}# Stores the paths to the models

    ActorDic={}# Stores all the actors
    ActorRefDic={}# Stores the paths to the actors
    ActorAnimsDic={}# Stores the animations for each actor
    blendAnimDict={}# Stores all the blended animations

    LightDict={}# Stores all the lights
    LightTypes={}# Stores types for the lights
    LightNodes={}# Stores the actual nodes for the lights

    dummyDict={}# Stores dummies

    collisionDict={}# Stores Collision information

    curveDict={}# Stores Mopath information
    curveIntervals=[]# Stores list of mopath intervals
    curveRefColl=[]# Stores paths to mopaths
    curveIntervalsDict={}# Stores mopath intervals

    particleDict={}# Stores particles
    particleNodes={}# Stores particle nodes

    #Light Count
    ambientCount=0
    directionalCount=0
    pointCount=0
    spotCount=0

    #Lighting Attribute
    lightAttrib = LightAttrib.makeAllOff()# Initialize lighting

    CollisionHandler=CollisionHandlerEvent()# Setup a Collision Handler
    ##########################################################################################################
    # Constructor: this is run first when you instantiate the SavedScene class
    ##########################################################################################################
    def __init__(self,loadmode=1,seParticleEffect=None,seParticles=None,executionpath=None):# loadmode 0 specifies that this file is being loaded by the scene editor and it passes its own versions of the particle fx modules

        self.loadmode=loadmode
        self.seParticleEffect=seParticleEffect
        self.seParticles=seParticles
        self.executionpath=executionpath

        base.enableParticles()# Enable Particle effects

        self.cTrav = CollisionTraverser() # Setup a traverser for collisions
        base.cTrav = self.cTrav
        self.CollisionHandler.setInPattern("enter%in")# The message to be raised when something enters a collision node
        self.CollisionHandler.setOutPattern("exit%in")# The message to be raised when something exits a collision node

        ##########################################################################################################
        # Code for all the models
        # To access these models:
        # theScene.ModelDic["'Model_Name"']
        # where theScene is the SavedScene class instance
        # Properties saved include:
        # Transformations
        # Alpha and color
        # Parent and child information
        ##########################################################################################################
        ##########################################################################################################
        # Code for all the Dummy Objects
        # To access the dummies
        # theScene.dummyDict['Dummy_Name']
        ##########################################################################################################
        ##########################################################################################################
        # Code for all the Actors and animations
        # To access the Actors
        # theScene.ActorDic['Actor_Name']
        # theScene.ActorDic['Actor_Name'].play('Animation_Name')
        ##########################################################################################################
        ##########################################################################################################
        # Code for setting up Collision Nodes
        # To use collision detection:
        # You must set up your own bitmasking and event handlers, the traverser "cTrav" is created for you at the top
        # The collision nodes are stored in collisionDict
        ##########################################################################################################

        ##########################################################################################################
        # Code for Lighting
        # To manipulated lights:
        # Manipulate the light node in theScene.LightNodes['Light_Name']
        ##########################################################################################################

        # Enable Ligthing
        render.node().setAttrib(self.lightAttrib)

        # Load Particle Effects. The parameters to this function are to allow us to use our modified versions of the Particle Effects modules when loading this file with the level editor
        self.starteffects(self.loadmode,self.seParticleEffect,self.seParticles)


        # Save Camera Settings
        camera.setX(0.0)
        camera.setY(-50.0)
        camera.setZ(10.0)
        camera.setH(-0.0)
        camera.setP(0.0)
        camera.setR(-0.0)
        camera.getChild(0).node().getLens().setNear(1.0)
        camera.getChild(0).node().getLens().setFar(100000.0)
        camera.getChild(0).node().getLens().setFov(VBase2(39.32012,30.00000))
        camera.getChild(0).node().getLens().setFilmSize(1.000,0.750)
        camera.getChild(0).node().getLens().setFocalLength(1.3995190858840942)
        camera.setTag("Metadata","")
        camera.reparentTo(render)
        base.disableMouse()
        base.setBackgroundColor(0.000,0.000,0.000)

        ##########################################################################################################
        # Motion Paths
        # Using Mopaths:
        # theScene.curveIntervals[0].start() or .loop() will play curve with index 0
        ##########################################################################################################

        ##########################################################################################################
        # Reparenting
        # A final pass is done on setting all the scenegraph hierarchy after all objects are laoded
        ##########################################################################################################


        ##########################################################################################################
        # Particle Effects
        # Using Particles:
        # theScene.enableeffect("Effect_Name")
        ##########################################################################################################

    def starteffects(self,mode,seParticleEffect=None,seParticles=None):
        return

    def enableeffect(self,effect_name):
        self.particleDict[effect_name].enable()
        return

    def disableeffect(self,effect_name):
        self.particleDict[effect_name].disable()
        return


        ##########################################################################################################
        # Animation Blending
        # Using blending:
        # theScene.playBlendAnim(actor,blendname)
        # theScene.stopBlendAnim(actor,blendname)
        # theScene.changeBlendAnim(actor,blendname,blend_amount)
        ##########################################################################################################

    def playBlendAnim(self,actor,blendName,loop=0):
        actor.enableBlend()
        blendDicts=self.blendAnimDict[actor.getName()]
        blendList=blendDicts[blendName]
        actor.setControlEffect(blendList[0],blendList[2])
        actor.setControlEffect(blendList[1],1.0-blendList[2])
        if(loop):
            actor.loop(blendList[0])
            actor.loop(blendList[1])
        else:
            actor.start(blendList[0])
            actor.start(blendList[1])

    def stopBlendAnim(self,actor,blendName):
        blendDicts=self.blendAnimDict[actor.getName()]
        blendList=blendDicts[blendName]
        actor.stop(blendList[0])
        actor.stop(blendList[1])

    def changeBlending(self,actor,blendName,blending):
        blendDicts=self.blendAnimDict[actor.getName()]
        blendList=blendDicts[blendName]
        blendList[2]=blending
        self.blendAnimDict[actor.getName()]={blendName:[blendList[0],blendList[1],blending]}


        ##########################################################################################################
        # Hide and Show Methods
        # These will help you hide/show dummies, collision solids, effect nodes etc.
        ##########################################################################################################


    def hideDummies(self):

        for dummy in self.dummyDict:
            self.dummyDict[dummy].reparentTo(hidden)

    def hideCollSolids(self):

        for collSolid in self.collisionDict:
            self.collisionDict[collSolid].hide()

    def hideEffectNodes(self):

        for effectnode in self.particleNodes:
            self.particleNodes[effectnode].hide()

    def showDummies(self):

        for dummy in self.dummyDict:
            self.dummyDict[dummy].reparentTo(hidden)

    def showCollSolids(self):

        for collSolid in self.collisionDict:
            self.collisionDict[collSolid].show()

    def showEffectNodes(self):

        for effectnode in self.particleNodes:
            self.particleNodes[effectnode].show()


        ##########################################################################################################
        # Particle Effects
        # This is where effect parameters are saved in a class
        # The class is then instantiated in the starteffects method and appended to the dictionaries
        ##########################################################################################################

