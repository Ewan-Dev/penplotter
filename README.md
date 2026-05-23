# penplotter
penplotter is a tool for converting images to plots on a sheet of paper. We use no image processing libraries for filters.

-@Ewan-Dev, @peiallll

## image process pipeline
1. resize
2. luminosity greyscale
3. Gaussian blur
4. Sobel operator
5. thresholding
6. Zhang-Suen thinning
7. cleanup
8. convert to paths


| before processing: | after processing: |
| -------- | -------- |
| <img src="/software/image-processing/images/teddybob.png" width=80px>   | <img src='/teddybob-lines.png' width=100px>   |
