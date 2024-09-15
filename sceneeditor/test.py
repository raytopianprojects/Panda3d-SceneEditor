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

        # Loading model's egg file
