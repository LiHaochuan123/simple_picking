"""wangyiheng"""
import time
from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import load
client = RemoteAPIClient()
sim = client.require('sim')
target_handle = sim.getObject('/UR5/target')
time.sleep(3)
sim.startSimulation()
shape1_handle = load.load_shape(simulation=sim, shape_size=[
    0.05, 0.05, 0.05], shape_position=[0.3, 0.3, 0.3])
time.sleep(2)
shape1_position = sim.getObjectPosition(shape1_handle)
sim.setObjectPosition(target_handle, shape1_position)
time.sleep(2)
sim.setIntProperty(sim.handle_scene, 'signal.RG2_open', 0)
time.sleep(2)
sim.setObjectPosition(target_handle, [-0.110, +0.37204, +0.51664])
time.sleep(2)
sim.setObjectPosition(target_handle, [-0.375, 0.5, 0.5])
time.sleep(2)
sim.setIntProperty(sim.handle_scene, 'signal.RG2_open', 1)
time.sleep(2)
sim.stopSimulation()
