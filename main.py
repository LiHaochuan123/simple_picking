"""Main function"""
import time
from coppeliasim_zmqremoteapi_client import RemoteAPIClient
client = RemoteAPIClient()
sim = client.require('sim')
targetHandle = sim.getObject('/UR5/target')
cubeHandle = sim.getObject('/Cuboid')
position = sim.getObjectPosition(cubeHandle)
time.sleep(3)
sim.startSimulation()
sim.setIntProperty(sim.handle_scene, 'signal.RG2_open', 1)
sim.setObjectPosition(targetHandle, position)
time.sleep(2)
# sim.setIntProperty(sim.handle_scene, 'signal.RG2_open', 1)
sim.setIntProperty(sim.handle_scene, 'signal.RG2_open', 0)
time.sleep(5)
sim.setObjectPosition(targetHandle, [-0.3, -0.3, 0.5])
time.sleep(5)
sim.stopSimulation()
