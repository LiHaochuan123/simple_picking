"""Main funcion ver1"""
import time
import random
from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import pick_and_place
import load

client = RemoteAPIClient()
sim = client.require('sim')
gripper_handle = sim.getObject('/UR5/target')
time.sleep(3)
sim.startSimulation()
sim.setIntProperty(sim.handle_scene, 'signal.RG2_open', 1)


handle_list = []
X = -0.2
Y = 0.3
A = 0.05
for i in range(5):
    c = load.load_shape(simulation=sim, shape_size=[
        A, A, A], shape_position=[X, Y, 0.3])
    handle_list.append(c)
    X += 0.1
    Y += 0.1
random.shuffle(handle_list)


for i in range(2):
    pick_and_place.pick_and_place_success(simulation=sim, shape_handle=handle_list[i],
                                          target_handle=gripper_handle, sleep_time=3)
h1, h2 = pick_and_place.pick_and_place_add(simulation=sim, shape_handle=handle_list[2],
                                           target_handle=gripper_handle, sleep_time=3,
                                           shape_size=[A, A, A])
handle_list.append(h1)
handle_list.append(h2)
pick_and_place.pick_and_place_success(simulation=sim, shape_handle=handle_list[3],
                                      target_handle=gripper_handle, sleep_time=3)
shape_position = sim.getObjectPosition(handle_list[4])
[x, y, z] = shape_position
sim.setObjectPosition(gripper_handle, [x, y, 0.3])
time.sleep(3)
sim.setObjectPosition(gripper_handle, [x, y, z])
time.sleep(0.25)
sim.removeObjects([handle_list[4]])
sim.setObjectPosition(gripper_handle, [x, y, 0.3])
time.sleep(3)
shape_position = sim.getObjectPosition(handle_list[5])
[x, y, z] = shape_position
sim.setObjectPosition(gripper_handle, [x, y, 0.3])
time.sleep(3)
sim.setObjectPosition(gripper_handle, [x, y, z])
time.sleep(3)
sim.setIntProperty(sim.handle_scene, 'signal.RG2_open', 0)
time.sleep(3)
sim.setObjectPosition(gripper_handle, [x, y, 0.3])
time.sleep(3)
sim.setObjectPosition(gripper_handle, [-y, -x, 0.3])
time.sleep(3)
sim.setObjectPosition(gripper_handle, [-y, -x, z])
time.sleep(3)
sim.setIntProperty(sim.handle_scene, 'signal.RG2_open', 1)
time.sleep(3)
sim.setObjectPosition(gripper_handle, [-y, -x, 0.3])
time.sleep(3)
pick_and_place.pick_and_place_success(simulation=sim, shape_handle=handle_list[6],
                                      target_handle=gripper_handle, sleep_time=3)
sim.setObjectPosition(gripper_handle, [-0.110, 0.37204, +0.51664])
time.sleep(3)


sim.stopSimulation()
