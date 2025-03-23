# Depth Map Generation Documentation
This project demonstrates how to compute a depth map from a pair of stereo images using OpenCV.

## Overview
#### Input: 
Two stereo images (left.png and right.png).

#### Processing: 
Convert images to grayscale, compute disparity using block matching, normalize the disparity, and apply a JET colormap.

#### Output: 
- A colorized depth map saved as depth.png.

```
OpenCV: pip install opencv-python

NumPy: pip install numpy
```
#### How to Run
Place left.png and right.png in the same directory as the script.
