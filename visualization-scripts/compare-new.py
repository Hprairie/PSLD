from skimage import transform, color, io
import sys
import matplotlib.pyplot as plt
from skimage.metrics import structural_similarity
import numpy as np

if __name__ == "__main__":
    img1 = io.imread(sys.argv[1])
    img2 = io.imread(sys.argv[2])
    img3 = io.imread(sys.argv[3])

    # Process the first image
    img1 = transform.resize(img1, (384, 384))  # Resize the image
    img1 = color.rgb2gray(img1)  # Convert the image to grayscale

    # Process the second image
    img2 = transform.resize(img2, (384, 384))  # Resize the image

    # Process the third image
    img3 = transform.resize(img3, (384, 384))  # Resize the image

    # Display the first image
    plt.subplot(1, 3, 1)
    plt.imshow(img1, cmap='gray')
    plt.title('Original')
    plt.axis('off')

    # Display the second image
    plt.subplot(1, 3, 2)
    plt.imshow(img2, cmap='gray')
    plt.title('Sample 1')
    plt.axis('off')

    # Display the difference
    plt.subplot(1, 3, 3)
    plt.imshow(img3, cmap='gray')
    plt.title('Sample 2')
    plt.axis('off')

    # Save the plot
    plt.savefig('results.png',  dpi=300, bbox_inches='tight')

    # Show the figure
    plt.show()
