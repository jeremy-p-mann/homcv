# Computes the betti numbers and Euler characteristic
# of the "dark regions" of an image.
# To do: make as a sklearn transformer


import numpy as np
from scipy import signal, ndimage
from scipy.ndimage.interpolation import shift
import networkx as nx


class betti_numbers:
    def __init__(self):
        pass

    def make_vertices(self, image):
        pass

    def make_edges(self, vertices):
        pass

    def make_faces(self, edges):
        pass

    def make_one_skeleton(self, vertices, edges):
        pass

    def compute_euler_char(self, vertices, edges, faces):
        pass

    def compute_connected_components(self, one_skeleton):
        pass

    def compute_betti_numbers(self, image, level):

        vertices = self.make_vertices(image)
        edges = self.make_edges(vertices)
        faces = self.make_faces(edges)
        one_skeleton = self.make_1_skeleton(vertices, edges, faces)

        e_char = self.compute_euler_char(vertices, edges, faces)

        b_0 = self.compute_connected_components(one_skeleton)
        b_1 = None  # b_0 - e_char

        betti_numbers = np.array([b_0, b_1], np.int8)

        return betti_numbers
