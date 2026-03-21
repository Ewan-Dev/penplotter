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

<section style="display:flex;flex-direction:row;gap:50px;">
<div style="display:flex;flex-direction:column;">
before processing:
<img src="/software/image-processing/images/teddybob.png" width=80px>
</div>
<div style="display:flex;flex-direction:column;">
after processing:
<img src='/teddybob-lines.png' width=100px>
</div>
</section>

## to-do
- path efficiency
- path to plots (stepper motors)
