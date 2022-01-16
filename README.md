# QuickHull


This is an implementation of the QuickHull algorithm in Python. It randomly generates a set of points and finds the convex hull of this set of points using the Quickhull algorithm. 

More details about QuickHull algorithm here: [Quickhull Algorithm](https://en.wikipedia.org/wiki/Quickhull) 
## Time Complexity


Time Complexity - O(n * log(r)) where __n__ = total no. of points, __r__ = no. of processed points 

Worst-case Scenario - total no. of points (n) = no. of processed points (r). Example below.

If this code helped you visualize and understand the Quickhull algorithm, please give this repo a star! :star:
## Results


Here are a couple of results:

![quickhull_20.gif](https://github.com/AnantJoshiCZ/QuickHull/blob/master/quickhull_20.gif)

Worst-case Scenario - Points in a Circle - Time Complexity O(n * log (n) )

![quickhull_20_circle.gif](https://github.com/AnantJoshiCZ/QuickHull/blob/master/quickhull_20_circle.gif)
# Installation/Setup

To get this code to run on your machine, you will need to follows these steps:

- Clone this repo to your local machine using 

```
git clone https://github.com/AnantJoshiCZ/QuickHull.git 
```

- Install John Zelle's graphics.py
```
pip install graphics.py
```
- Run quickhull.py
### MacOS

If you're on the MacOS, you may need to install the Tkinter dependencies separately. To do this with Homebrew, use the following:
```
brew install python-tk
```
This will install any Tkinter/tkinter dependencies and allow you to use the graphics.py library. If you do not do this step, you may see an error when running the code. This is a common issue with the graphics.py library which is supposed to be a library for learning basic graphic concepts.
