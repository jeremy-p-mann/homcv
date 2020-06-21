from .context import homcv
from homcv.betti_numbers import betti_numbers
import numpy as np


def test_disk():
    disk = np.zeros((10, 10))
    disk[1:4, 1: 4] = 1
    bn = betti_numbers()
    assert bn.compute_betti_numbers(disk, .5)[0] == 1, (
        'Disk has 1 connected component')
    assert bn.compute_betti_numbers(disk, .5)[1] == 0, (
        'Disk has 0 first homology classes')


def test_circle():
    circle = np.zeros((10, 10))
    circle[[1, 3], 1: 4] = 1
    circle[1:4, [1, 3]] = 1
    bn = betti_numbers()
    assert bn.compute_betti_numbers(circle, .5)[0] == 1, (
        'Circle has 1 connected component')
    assert bn.compute_betti_numbers(circle, .5)[1] == 1, (
        'Circle has 1 first homology class')


def test_figure_eight():
    figure_eight = np.zeros((10, 10))
    figure_eight[[1, 3], 1: 8] = 1
    figure_eight[1:4, [1, 3, 7]] = 1
    bn = betti_numbers()
    assert bn.compute_betti_numbers(figure_eight, .5)[0] == 1, (
        'Figure eight has 1 connected component')
    assert bn.compute_betti_numbers(figure_eight, .5)[1] == 2, (
        'Figure eight has 1 first homology classes')


def test_two_circles():
    two_circles = np.zeros((10, 10))
    two_circles[[1, 3], 1: 4] = 1
    two_circles[[1, 3], 5: 7] = 1
    two_circles[1:4, [1, 3, 5, 7]] = 1
    bn = betti_numbers()
    assert bn.compute_betti_numbers(two_circles, .5)[0] == 2, (
        'Two circles has 2 connected components')
    assert bn.compute_betti_numbers(two_circles, .5)[1] == 2, (
        'Two circles has two first homology classes')
