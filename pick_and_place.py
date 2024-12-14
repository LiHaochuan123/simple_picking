"""This module picking and placing objects."""
import time
from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import load


def pick_and_place_success(
        simulation, shape_handle: int, target_handle: int, sleep_time: int) -> None:
    """Function picking and placing an object successfully.

    args:
        simulation:
        shape_handle: handle of shape
        target_handle: handle of target
    """
    time.sleep(sleep_time)
    shape_position = simulation.getObjectPosition(shape_handle)
    [x, y, z] = shape_position
    simulation.setObjectPosition(target_handle, [x, y, 0.3])
    time.sleep(sleep_time)
    simulation.setObjectPosition(target_handle, [x, y, z])
    time.sleep(sleep_time)
    simulation.setIntProperty(simulation.handle_scene, 'signal.RG2_open', 0)
    time.sleep(sleep_time)
    simulation.setObjectPosition(target_handle, [x, y, 0.3])
    time.sleep(sleep_time)
    simulation.setObjectPosition(target_handle, [-y, -x, 0.3])
    time.sleep(sleep_time)
    simulation.setObjectPosition(target_handle, [-y, -x, z])
    time.sleep(sleep_time)
    simulation.setIntProperty(simulation.handle_scene, 'signal.RG2_open', 1)
    time.sleep(sleep_time)
    simulation.setObjectPosition(target_handle, [-y, -x, 0.3])
    time.sleep(sleep_time)


def pick_and_place_add(
        simulation, shape_handle: int, target_handle: int, sleep_time: int,
        shape_size: list) -> None:
    """Function adding three objects on existed object and picking and placing successfully.

    args:
        simulation:
        shape_handle: handle of shape
        target_handle: handle of target
    """
    time.sleep(sleep_time)
    shape_position = simulation.getObjectPosition(shape_handle)
    [x, y, z0] = shape_position
    simulation.setObjectPosition(target_handle, [x, y, 0.3])
    time.sleep(1)
    add_shape_handle0 = load.load_shape(simulation=simulation, shape_size=shape_size,
                                        shape_position=[x, y, z0+0.1])
    add_shape_handle1 = load.load_shape(simulation=simulation, shape_size=shape_size,
                                        shape_position=[-0.2, 0.5, z0+0.1])
    add_shape_handle2 = load.load_shape(simulation=simulation, shape_size=shape_size,
                                        shape_position=[-0.2, 0.7, z0+0.1])
    time.sleep(sleep_time)
    shape_position = simulation.getObjectPosition(add_shape_handle0)
    [x, y, z1] = shape_position
    simulation.setObjectPosition(target_handle, [x, y, z1])
    time.sleep(sleep_time)
    simulation.setIntProperty(simulation.handle_scene, 'signal.RG2_open', 0)
    time.sleep(sleep_time)
    simulation.setObjectPosition(target_handle, [x, y, 0.3])
    time.sleep(sleep_time)
    simulation.setObjectPosition(target_handle, [-y, -x, 0.3])
    time.sleep(sleep_time)
    simulation.setObjectPosition(target_handle, [-y, -x, z0])
    time.sleep(sleep_time)
    simulation.setIntProperty(simulation.handle_scene, 'signal.RG2_open', 1)
    time.sleep(sleep_time)
    simulation.setObjectPosition(target_handle, [-y, -x, 0.3])
    time.sleep(sleep_time)
    simulation.setObjectPosition(target_handle, [x, y, 0.3])
    time.sleep(sleep_time)
    simulation.setObjectPosition(target_handle, [x, y, z0])
    time.sleep(sleep_time)
    simulation.setIntProperty(simulation.handle_scene, 'signal.RG2_open', 0)
    time.sleep(sleep_time)
    simulation.setObjectPosition(target_handle, [x, y, 0.3])
    time.sleep(sleep_time)
    simulation.setObjectPosition(target_handle, [-0.5, -0.2, 0.3])
    time.sleep(sleep_time)
    simulation.setObjectPosition(target_handle, [-0.5, -0.2, z0])
    time.sleep(sleep_time)
    simulation.setIntProperty(simulation.handle_scene, 'signal.RG2_open', 1)
    time.sleep(sleep_time)
    simulation.setObjectPosition(target_handle, [-0.5, -0.2, 0.3])
    time.sleep(sleep_time)
    return add_shape_handle1, add_shape_handle2


def pick_and_place_hand(
        simulation, shape_handle: int, target_handle: int, hand_handle: int, sleep_time: int) -> None:
    """Function picking an object and placing on a human hand.

    args:
        simulation:
        shape_handle: handle of shape
        target_handle: handle of target
    """
    time.sleep(sleep_time)
    shape_position = simulation.getObjectPosition(shape_handle)
    [x, y, z] = shape_position
    simulation.setObjectPosition(target_handle, [x, y, 0.3])
    time.sleep(sleep_time)
    simulation.setObjectPosition(target_handle, [x, y, z])
    time.sleep(sleep_time)
    simulation.setIntProperty(simulation.handle_scene, 'signal.RG2_open', 0)
    time.sleep(sleep_time)
    simulation.setObjectPosition(target_handle, [x, y, 0.3])
    time.sleep(sleep_time)
    hand_position = simulation.getObjectPosition(hand_handle)
    [x, y, z] = hand_position
    simulation.setObjectPosition(target_handle, [x+0.0265, y+0.00551, 0.3])
    time.sleep(sleep_time)
    simulation.setObjectPosition(
        target_handle, [x+0.0265, y+0.00551, z+0.00658])
    time.sleep(sleep_time)
    simulation.setIntProperty(simulation.handle_scene, 'signal.RG2_open', 1)
    time.sleep(sleep_time)
    simulation.setObjectPosition(target_handle, [x+0.0265, y+0.00551, 0.3])
    time.sleep(sleep_time)


if __name__ == "__main__":
    client = RemoteAPIClient()
    sim = client.require('sim')
    time.sleep(3)
    sim.startSimulation()
    target1_handle = sim.getObject('/UR5/target')
    sim.setIntProperty(sim.handle_scene, 'signal.RG2_open', 1)
    shape1_handle = load.load_shape(simulation=sim, shape_size=[
                                    0.05, 0.05, 0.05], shape_position=[0.2, 0.2, 0.3])
    shape2_handle = load.load_shape(simulation=sim, shape_size=[
                                    0.05, 0.05, 0.05], shape_position=[0.3, 0.3, 0.3])
    shape3_handle = load.load_shape(simulation=sim, shape_size=[
                                    0.05, 0.05, 0.05], shape_position=[0.2, 0.4, 0.3])
    pick_and_place_success(simulation=sim, shape_handle=shape1_handle,
                           target_handle=target1_handle, sleep_time=2)
    sim.stopSimulation()
