"""This module loads objects."""
import time
from coppeliasim_zmqremoteapi_client import RemoteAPIClient
client = RemoteAPIClient()
sim = client.require('sim')
time.sleep(3)
sim.startSimulation()
shapeHandle = sim.createPrimitiveShape(
    sim.primitiveshape_cuboid, [0.05, 0.05, 0.05])
sim.setObjectPosition(shapeHandle, [0.5, 0.5, 0.5])
sim.setBoolProperty(shapeHandle, 'respondable', True)
sim.setBoolProperty(shapeHandle, 'dynamic', True)
time.sleep(5)
sim.stopSimulation()
