
# Image PMF Calculation and Visualization

This Python script performs analysis on a set of images to calculate and visualize the Probability Mass Function (PMF) of pixel intensities. It includes functionality to handle individual images, combine multiple images, and display the resulting PMF.

## Requirements

- Python 3.x
- `numpy`
- `matplotlib`

You can install the required packages using pip:

```bash
pip install numpy matplotlib
```

## Functionality

1. **Calculate PMF for Individual Images**
   - Computes the PMF of pixel intensities for each image.
   - Displays a bar chart showing the PMF.

2. **Combine and Analyze Images**
   - Adds pixel values of a specified subset of images.
   - Calculates and displays the PMF for the combined image.

## Script Overview

### Functions

- **`calculate_pmf(image)`**
  - Converts the image to grayscale (if necessary).
  - Computes the histogram of pixel intensities.
  - Calculates the PMF from the histogram.
  - Returns the bin edges and PMF values.

- **`plot_pmf(bin_edges, pmf, title='Olasılık Kütle Fonksiyonu (PMF)')`**
  - Plots the PMF as a bar chart.
  - Displays the chart with appropriate labels and title.

- **`add_images(images)`**
  - Adds pixel values of the images in the provided list.
  - Returns the resulting combined image.

- **`display_menu(menu)`**
  - Displays a menu of options to the user.

- **`main()`**
  - Main function that handles user input and performs the requested operations based on menu selection.

### Usage

1. **Update Image Paths**

   Modify the `image_paths` list in the `main()` function to point to the correct locations of your images.

   ```python
   image_paths = [
       "path/to/image1.tiff",
       "path/to/image2.tiff",
       ...
   ]
   ```

2. **Run the Script**

   Execute the script using Python:

   ```bash
   python script_name.py
   ```

3. **Interact with the Menu**

   The script presents a menu with the following options:

   - `1`: Calculate and show the PMF for each individual image.
   - `2`: Combine the first 3 images, calculate, and show the PMF.
   - `3`: Combine the first 6 images, calculate, and show the PMF.
   - `4`: Exit the script.

## Notes

- The images should be in a format that can be read by `matplotlib.pyplot.imread`.
- The script assumes the images are in TIFF format and grayscale or RGB. For RGB images, the script converts them to grayscale for PMF calculation.
- Ensure that the paths to the images are correct and that the images exist at those paths.
