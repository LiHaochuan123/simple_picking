"""This module loading objects."""
import time
import random
from coppeliasim_zmqremoteapi_client import RemoteAPIClient


def load_shape(simulation, shape_size: list, shape_position: list) -> int:
    """Function loading a cuboid in specific position.

    args:
        simulation:
        shape_size: list of shape box size
        shape_position: list of shape position
    return:
        shape_handle: handle of shape 
    """
    shape_handle = simulation.createPrimitiveShape(
        simulation.primitiveshape_cuboid, shape_size)
    simulation.setObjectPosition(shape_handle, shape_position)
    simulation.setBoolProperty(shape_handle, 'respondable', True)
    simulation.setBoolProperty(shape_handle, 'dynamic', True)
    shape_name = simulation.getObjectAlias(shape_handle, 2)
    random_color = [random.uniform(0.5, 1) for _ in range(3)]
    simulation.setShapeColor(
        shape_handle, "", simulation.colorcomponent_ambient_diffuse, random_color)
    print(f'Loading shape succeed!\nshape name: {shape_name}')
    print(f'shape size: {shape_size}\nshape position: {shape_position}')
    print(f"shape handle {shape_handle}\n")
    return shape_handle


if __name__ == "__main__":
    client = RemoteAPIClient()
    sim = client.require('sim')
    time.sleep(3)
    sim.startSimulation()
    for i in range(3):
        a = random.uniform(0.03, 0.05)
        a = round(a, 2)
        b = random.uniform(0.4, 0.5)
        b = round(b, 2)
        load_shape(simulation=sim, shape_size=[
            a, a, a], shape_position=[b, b, b])
    time.sleep(5)
    sim.stopSimulation()
