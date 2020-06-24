# HomCV: Homotopical Computer Vision 

HomCV is a Python library deploying homotopy theoretic methods to computer vision.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install HomCV.

```bash
pip install homcv
```

## Examples

```python
import homcv
from skimage.color import rgb2gray
import matplotlib.image as mpimg


disk_image = mpimg.imread('pic_of_disk.png')
circle_image = mpimg.imread('pic_of_circle.png')
figure_eight_image = mpimg.imread('pic_of_figure_eight.png')
two_circles_image = mpimg.imread('pic_of_two_circles.png')

disk_gs_image = rgb2gray(disk_image)
circle_gs_image = rgb2gray(circle_image)
figure_eight_gs_image = rgb2gray(figure_eight_image)
two_circles_gs_image = rgb2gray(two_circles_image)

bn = betti_numbers()

bn.compute_betti_numbers(disk_gs_image, level = 0.5) 
# returns [1, 0]
bn.compute_betti_numbers(circle_gs_image, level = 0.5) 
# returns [1, 1]
bn.compute_betti_numbers(figure_eight_gs_image, level = 0.5) 
# returns [1, 2]
bn.compute_betti_numbers(two_circles_gs_image, level = 0.5) 
# returns [2, 2]
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)