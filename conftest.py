import pytest
import numpy as np


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
