'''
Computes the betti numbers and Euler characteristic
of the "dark regions" of an image.
'''


import numpy as np

from . import utils


def betti_numbers(image, threshold=.5):
    '''
    Computes the zeroeth and first Betti numbers of the "dark" region of a
    greyscale image.

    Note that the second Betti number must be zero.

    Parameters
    ----------
    image: ndarray, shape (nx, ny)
        Numpy array representing a greyscale image
    threshold: float
        Number specifying the "data"

    Returns
    -------
    [betti_0, betti_1] : ndarray, shape (2,)
        Zeroeth and first betti numbers of the regions of the image
        greater than the specified threshold.

    '''
    vertices = utils._make_vertices(image, threshold)
    edges = utils._make_edges(vertices)
    faces = utils._make_faces(edges)
    one_skel = utils._make_one_skeleton(vertices, edges)

    euler_char = utils._compute_euler_char(vertices, edges, faces)

    betti_0 = utils._compute_connected_components(one_skel)
    betti_1 = betti_0 - euler_char

    betti_numbers = np.array([betti_0, betti_1], np.int8)

    return betti_numbers


