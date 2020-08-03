import numpy as np

from .context import homcv
from homcv import betti_numbers


def test_disk_betti_numbers(disk):
    assert betti_numbers(disk, .5)[0] == 1, (
        'Disk has 1 connected component')
    assert betti_numbers(disk, .5)[1] == 0, (
        'Disk has 0 first homology classes')


def test_circle_betti_numbers(circle):
    assert betti_numbers(circle, .5)[0] == 1, (
        'Circle has 1 connected component')
    assert betti_numbers(circle, .5)[1] == 1, (
        'Circle has 1 first homology class')


def test_figure_eight_betti_numbers(figure_eight):
    assert betti_numbers(figure_eight, .5)[0] == 1, (
        'Figure eight has 1 connected component')
    assert betti_numbers(figure_eight, .5)[1] == 2, (
        'Figure eight has 1 first homology classes')


def test_two_circles_betti_numbers(two_circles):
    assert betti_numbers(two_circles, .5)[0] == 2, (
        'Two circles has 2 connected components')
    assert betti_numbers(two_circles, .5)[1] == 2, (
        'Two circles has two first homology classes')

