import numpy as np

#the total hydrographic system
#this is comprised of various numpy matrices which store info about the system
class system():
    def __init__(self,cell_length,grid_size,elevation_map,conductivity_map,erodability_map,fluid_density=1000,gravity=9.81,dynamic_visocity=0.00089):
        self.cell_length = cell_length #length of a cell in metres
        self.cell_size = self.cell_length*self.cell_length #size of a cell in square meters
        self.grid_size = grid_size #number of cells in  x,y axis
        self.elevation_map = elevation_map #elevation of the centre of each grid cell in metres above sea level
        self.conductivity_map = conductivity_map #how hydraulically conductive is the ground
        self.erodability_map = erodability_map #how erodable is the ground
        self.fluid_density = fluid_density #density of the fluid, kg/m^3, default for fresh water
        self.gravity = gravity #gravity acceleration, m/s^2, default for earth
        self.dynamic_visocity = dynamic_visocity #dynamic viscoity, default for fresh water



