# Name:                                            Renacin Matadeen
# Date:                                               12/15/2020
# Title                                          Particle Simulation
#
# ----------------------------------------------------------------------------------------------------------------------
import time
import pyglet
from pyglet.gl import *
import math
# ----------------------------------------------------------------------------------------------------------------------
"""
Notes:
    + Following:
        - https://www.youtube.com/watch?v=Wyv5TnkFuxE
        - https://www.youtube.com/channel/UCN7uBodTAg8KcsuDiJ9u4Rg

"""
# ----------------------------------------------------------------------------------------------------------------------

class Triangle:
    def __init__(self):
        self.vertices = pyglet.graphics.vertex_list(3, ("v3f", [-0.5, -0.5, 0.0,   0.5, -0.5, 0.0,   0.0, 0.5, 0.0]),
                                                       ("c3B", [100, 200, 220,  200, 110, 100,  100, 250, 100])
                                                       )




# Use Pyglet As ENV, Create Window Class
class MainWindow(pyglet.window.Window):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_minimum_size(200, 200)
        self.triangle = Triangle()

    def on_draw(self):
        self.triangle.vertices.draw(GL_TRIANGLES)
# ----------------------------------------------------------------------------------------------------------------------

# Main Entry Point Into Python Code
if __name__ == "__main__":
    window = MainWindow(800, 800, "Main Window", resizable=True)
    window.on_draw()
    pyglet.app.run()
