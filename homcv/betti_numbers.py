# Computes the betti numbers and Euler characteristic
# of the "dark regions" of an image.
# To do: make as a sklearn transformer


import numpy as np
from scipy.ndimage.interpolation import shift
import networkx as nx


class betti_numbers:
    def __init__(self):
        pass

    def make_vertices(self, image, level):
        '''
        Returns the subobject classifier of the partition of the image
        into light=False (less than level) and dark=True (greater than level)
        A nonzero entry
        '''
        vertices = (image > level).astype(np.int8)
        return vertices

    def make_edges(self, vertices):
        '''
        Creates an array recording whether there exists an adjacent
        dark

        Input
        -----
        vertices = numpy array of "vertices"

        Output
        ------
        edges = numpy array of (vertices.shape, 4).

        edges[x, y, k] indicates that there is a dark pixel at
        (x, y) and at (x, y) + direction[k], where:
        direction[0] = right
        direction[1] = up
        direction[2] = left
        direction[3] = down
        '''

        # directions are [left, down, right, up]
        directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]

        list_of_edges = [vertices & shift(vertices, direction)
                         for direction in directions]

        edges = np.dstack(list_of_edges)

        return edges

    def make_faces(self, edges):

        bottom_left_corner = edges[:, :, 1] & edges[:, :, 0]
        top_right_corner = edges[:, :, 3] & edges[:, :, 2]

        print('bottom_left_corner', bottom_left_corner.sum())
        print('top_right_corner', top_right_corner.sum())

        faces = bottom_left_corner & shift(top_right_corner, [-1, -1])
        return faces

    def make_one_skeleton(self, vertices, edges):
        '''
        Assembles edges and vertices into a networkx graph
        '''
        one_skel = nx.Graph()

        one_skel.add_nodes_from(zip(*np.nonzero(vertices)))

        hor_0 = zip(*np.nonzero(edges[:, :, 0]))
        hor_1 = zip(*np.nonzero(edges[:, :, 2]))
        hor_edges = zip(hor_0, hor_1)

        vert_0 = zip(*np.nonzero(edges[:, :, 1]))
        vert_1 = zip(*np.nonzero(edges[:, :, 3]))
        vert_edges = zip(vert_0, vert_1)

        one_skel.add_edges_from(hor_edges)
        one_skel.add_edges_from(vert_edges)

        return one_skel

    def compute_euler_char(self, vertices, edges, faces):
        # vertices - horizontal edges - vertical edges + faces
        e_char = vertices.sum() - edges[:, :, [0, 1]].sum() + faces.sum()
        return e_char

    def compute_connected_components(self, one_skel):
        b_0 = nx.number_connected_components(one_skel)
        return b_0

    def compute_betti_numbers(self, image, level):

        vertices = self.make_vertices(image, level)
        edges = self.make_edges(vertices)
        faces = self.make_faces(edges)
        one_skel = self.make_one_skeleton(vertices, edges)

        e_char = self.compute_euler_char(vertices, edges, faces)

        b_0 = self.compute_connected_components(one_skel)
        b_1 = b_0 - e_char

        betti_numbers = np.array([b_0, b_1], np.int8)

        return betti_numbers


def single_point_test():
    # test for a single point
    pass


def horizontal_edge_test():
    pass


def vertical_edge_test():
    pass


def square_test():
    # test for a single square
    pass
