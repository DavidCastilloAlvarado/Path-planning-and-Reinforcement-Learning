# Finding obstacles
in this section we will learn how to finde obstacles into any picture

# Pipelines:
This is the way that we achieve our aim. 
1. GaussianBlur
2. Get the range of values in HSV
 for the obstacles
3. Take only the pixels that match with the ranges into a bit map
4. Clean up the bit map
5. Fill small gaps
6. Remove specks
7. Dilate the mask
8. convexify figures
