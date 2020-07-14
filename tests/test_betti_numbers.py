import numpy as np
import pytest

from .context import betti_numbers


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

@pytest.fixture(scope='session')
def disk():
    disk = np.zeros((10, 10))
    disk[1:4, 1: 4] = 1
    return disk

@pytest.fixture(scope='session')
def circle():
    circle = np.zeros((10, 10))
    circle[[1, 3], 1: 4] = 1
    circle[1:4, [1, 3]] = 1
    return circle


@pytest.fixture(scope='session')
def figure_eight():
    figure_eight = np.zeros((10, 10))
    figure_eight[[1, 3], 1: 8] = 1
    figure_eight[1:4, [1, 3, 7]] = 1
    return figure_eight


@pytest.fixture(scope='session')
def two_circles():
    two_circles = np.zeros((10, 10))
    two_circles[[1, 3], 1: 4] = 1
    two_circles[[1, 3], 5: 7] = 1
    two_circles[1:4, [1, 3, 5, 7]] = 1
    return two_circles
