"""This module loading objects."""
import time
from coppeliasim_zmqremoteapi_client import RemoteAPIClient


def load_shape(simulation: RemoteAPIClient.require) -> None:
    """Function loading a cuobid in specific position.

    args:
        simulation: 
    """
    shape_handle = simulation.createPrimitiveShape(
        simulation.primitiveshape_cuboid, [0.05, 0.05, 0.05])
    simulation.setObjectPosition(shape_handle, [0.5, 0.5, 0.5])
    simulation.setBoolProperty(shape_handle, 'respondable', True)
    simulation.setBoolProperty(shape_handle, 'dynamic', True)


if __name__ == "__main__":
    client = RemoteAPIClient()
    sim = client.require('sim')
    time.sleep(3)
    sim.startSimulation()
    load_shape(simulation=sim)
    time.sleep(5)
    sim.stopSimulation()
