# penplotter
penplotter is a tool for converting images to plots on a sheet of paper. We aim to use no image processing libraries for filters.

## image process pipeline
1. resize
2. luminosity greyscale
3. Gaussian blur
4. Sobel operator
5. thresholding
6. Zhang-Suen thinning
7. cleanup
8. convert to paths

## to-do
- path efficiency
- path to plots (stepper motors)
