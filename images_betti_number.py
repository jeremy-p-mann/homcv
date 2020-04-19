import numpy as np
import matplotlib.pyplot as plt
from scipy import signal, ndimage
from scipy.ndimage import shift as trans
import networkx as nx


def vertices(level, image):
    '''
    Returns the subobject classifier of the partition of the image
    into light = 0 (less than level) and dark = 1 (greater than level)
    A nonzero entry
    Input:
    -----
    image = 2D numpy array = input grayscale image

    level = number, specifuing the threshold which specifies
            the dark regions (greater than level) and light regions
            (less than level)
    Output:
    -------
    vertics = binary numpy array, same shape as the input.
              nonzero entries = dark regions, which one
              thinks of as a vertex of a graph we're building 
    '''
    vertices = np.zeros(image.shape)[:, :, ]
    vertices[image > level] = 1
    return vertices

# The order is (0) up, (1) right, (2) down, (3) left
def edges(v):
    '''
    Creates an array recording whether there exists an adjacent
    dark
    The order is (0) up, (1) right, (2) down, (3) left
    Input
    -----
    v = numpy array of "vertices"
    Output
    ------
    edges = numpy array of (v.shape, 4).
            An entry at (i, j, tau) is one if there is a vertex at the (i,j)
            spot of
    '''
    dir = [[0, -1], [-1, 0], [0, 1], [1, 0]]
    edges = np.dstack([v * trans(i, v) for i in dir] )
    return edges

def faces(e):
    '''
    Input
    -----

    Output
    ------

    '''
    dir = [[-1, -1], [-1, 1], [1, 1], [1, -1]]
    i = 0
    faces = e[:,:,i]*e[:,:,i - 3]*trans(dir[i], e[:,:,i - 1] * e[:,:,i - 2])
    return faces

def euler_char(level, image):
    v = vertices(level, image)
    e = edges(v)
    f = faces(e)
    # vertices - horizontal edges - vertical edges + faces
    chi = v.sum() - e[:, :, [0,1]].sum() + f.sum()
    return chi

# Outputs a graph from the vertex and edge data
def skeleton_1(v, e):
    # create a graph
    skel_1 = nx.Graph()
    # add the nodes, which are the (x,y) position of the vertices
    nodes = skel_1.add_nodes_from(zip(*np.nonzero(v)))

    # Now the edges, first the horizontal followed by the vertical

    # recall indices are (0) = up, (1) = right, (2) = down, (3) = left
    # the right = (1) boundary of the horizontal edges
    hor_0 = zip(*np.nonzero(e[:,:, 1]))
    # the left = (3) boundary of the horizontal edges
    hor_1 = zip(*np.nonzero(e[:, :, 3]))
    # combined to obtain the right edges
    hor_edges = zip(hor_0, hor_1)
    # the up = (0) boundary of the vertical edges
    vert_0 = zip(*np.nonzero(e[:, :, 0]))
    # the down = (2) boundary of the vertical edges
    vert_1 = zip(*np.nonzero(e[:, :, 2]))
    # combined to obtain the vertical edges
    vert_edges = zip(vert_0, vert_1)
    # add the horizontal edges
    skel_1.add_edges_from(hor_edges)
    # add the vertical edges
    skel_1.add_edges_from(vert_edges)
    return skel_1

# inputs the 1-skeleton (as a networkx graph)
# returns a list of [b_0, b_1]
def betti_numbers(image, level):
    v = vertices(level, image)
    e = edges(v)
    f = faces(e)
    skel_1 = skeleton_1(v, e)
    # count the number of connected components
    b_0 = nx.number_connected_components(skel_1)
    print(b_0, type(b_0))
    # compute the Euler Characteristic
    e_char = chi = v.sum() - e[:, :, [0,1]].sum() + f.sum()
    # compute the first betti number
    b_1 = b_0 - e_char
    return [b_0, b_1]
