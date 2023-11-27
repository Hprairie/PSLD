from skimage import transform, color, io
import sys
import matplotlib.pyplot as plt
from skimage.metrics import structural_similarity
import numpy as np

if __name__ == "__main__":
    img1 = io.imread(sys.argv[1])
    img2 = io.imread(sys.argv[2])

    # Process the first image
    img1 = transform.resize(img1, (384, 384))  # Resize the image
    img1 = color.rgb2gray(img1)  # Convert the image to grayscale

    # Process the second image
    img2 = transform.resize(img2, (384, 384))  # Resize the image

    assert img1.shape == img2.shape, "Images are not the same size"


    # The 'diff' image contains the difference map, scale it to the range [0, 1]
    score, diff = structural_similarity(img1, img2, data_range=255, full=True)
    diff = np.power(diff, 400)
    # Display the first image
    plt.subplot(1, 3, 1)
    plt.imshow(img1, cmap='gray')
    plt.title('Image 1')

    # Display the second image
    plt.subplot(1, 3, 2)
    plt.imshow(img2, cmap='gray')
    plt.title('Image 2')

    # Display the difference
    plt.subplot(1, 3, 3)
    plt.imshow(diff, cmap='gray')
    plt.title('Difference')

    # Show the figure
    plt.show()
    print(score)
