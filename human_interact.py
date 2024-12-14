"""human_interact"""
import time
import random
from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import load
import pick_and_place


client = RemoteAPIClient()
sim = client.require('sim')
gripper_handle = sim.getObject('/UR5/target')
hand = sim.getObject('/Group')
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
time.sleep(3)


for item in handle_list:
    x_hand = random.uniform(-0.7, -0.3)
    y_hand = random.uniform(-0.2, 0.2)
    hand_position = sim.getObjectPosition(hand)
    [_, _, z_hand] = hand_position
    sim.setObjectPosition(hand, [x_hand, y_hand, z_hand])
    time.sleep(3)
    pick_and_place.pick_and_place_hand(simulation=sim, shape_handle=item,
                                       target_handle=gripper_handle, hand_handle=hand, sleep_time=3)
    time.sleep(1)
    sim.removeObjects([item])
    time.sleep(3)


sim.stopSimulation()
