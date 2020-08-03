'''
Various useful functions, most of which build intermediate objects
'''

import numpy as np
from scipy.ndimage.interpolation import shift
import networkx as nx


def _make_vertices(image, threshold):
    '''
    Returns a 2 dimensional array indicating the presence of a pixel darker
    than a specified threshold.

    In other words, the subobject classifier of the partition of the image
    into light=0 (less than level) and dark=1 (greater than level).

    Parameters
    ----------
    image : ndararay, shape (nx, ny)
        2 dimensional array representing the image
    threshold : float, optional, default to .5
        Float indicating the lowest value considered "dark"

    Returns
    -------
    vertices : ndarray, shape (nx,  ny)
        vertices[x, y] == 1 indicates that image[x, y] >= threshold
        vertices[x, y] == 0 indicates that image[x, y] < threshold

    '''
    assert image.ndim == 2, 'input must be two dimensional'
    vertices = (image >= threshold).astype(np.int8)
    return vertices


def _make_edges(vertices):
    '''
    Creates a 3 dimensional array recording whether there exists adjacent
    vertices.

    Parameters
    ----------
    vertices : ndarray, shape (nx, ny)

    Returns
    -------
    edges : ndarray, shape (nx, ny, 4)
        edges[x, y, k]  == 1 indicates that there is a dark pixel at
        (x, y) and at (x, y) + v[k], where:
        v[0] = right
        v[1] = up
        v[2] = left
        v[3] = down

        Note the directions start at 0 (viewed as a complex number),
        and move counterclockwise by 90 degrees

    '''
    directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]  # [left, down, right, up]

    list_of_edges = [vertices & shift(vertices, direction)
                     for direction in directions]

    edges = np.dstack(list_of_edges)
    return edges


def _make_faces(edges):
    '''
    Creates a 2 dimensional array indicating the presence of the
    bottom left corner of four adjacent pixels forming a square.

    Parameters
    ----------
    edges : ndarray, shape (nx, ny, 4)
        Array representing the presence of adjacent dark pixels

    Returns
    -------
    faces : ndarray, shape (nx, ny)
        faces[x, y] == 1 indicates that there is dark pixel at
        [x, y], [x, y]+right, [x, y]+up, and [x, y]+up+right

    '''
    bottom_left_corner = edges[:, :, 1] & edges[:, :, 0]
    top_right_corner = edges[:, :, 3] & edges[:, :, 2]

    faces = bottom_left_corner & shift(top_right_corner, [-1, -1])
    return faces


def _make_one_skeleton(vertices, edges):
    '''Assembles edges and vertices into a networkx graph'''
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


def _compute_connected_components(one_skel):
    b_0 = nx.number_connected_components(one_skel)
    return b_0


def _compute_euler_char(vertices, edges, faces):
    ''' Computes the Euler characteristic using the vertexs/edges/faces'''
    # vertices - (right edges + up edges) + faces
    euler_char = vertices.sum() - edges[:, :, [0, 1]].sum() + faces.sum()
    return euler_char
