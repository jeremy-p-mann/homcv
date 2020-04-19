# homology_of_greyscale_images

Vectorized computation of the Betti numbers and Euler characteristic of the "dark region" of a greyscale image.

If you're interested in learning some basics of Topological Data Analysis this can serve as a good introduction.

Code relies primarily on numpy and networkx. At a mathematical level, the code uses Alexander duality 
to reduce the computation of the first betti number ("number of loops") of the dark region to the 
connected components of the light regions ("number of holes")
