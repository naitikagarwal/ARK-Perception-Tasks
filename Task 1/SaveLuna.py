import cv2
import numpy as np

def main():
    
    img_left = cv2.imread('left.png', cv2.IMREAD_COLOR)
    img_right = cv2.imread('right.png', cv2.IMREAD_COLOR)

    if img_left is None or img_right is None:
        raise IOError("Error loading one or both images. Please check the file paths.")

    # Step 2: Convert the images to grayscale
    gray_left = cv2.cvtColor(img_left, cv2.COLOR_BGR2GRAY)
    gray_right = cv2.cvtColor(img_right, cv2.COLOR_BGR2GRAY)

    # StereoBM object and compute the disparity map
    num_disparities = 64
    block_size = 15
    stereo = cv2.StereoBM_create(numDisparities=num_disparities, blockSize=block_size)
    disparity = stereo.compute(gray_left, gray_right)

    disparity_normalized = cv2.normalize(
        disparity,
        None,
        alpha=0,
        beta=255,
        norm_type=cv2.NORM_MINMAX,
        dtype=cv2.CV_8U
    )

    depth_heatmap = cv2.applyColorMap(disparity_normalized, cv2.COLORMAP_JET)
    cv2.imwrite('depth.png', depth_heatmap)
    print("Depth heatmap saved as 'depth.png'")

if __name__ == "__main__":
    main()
