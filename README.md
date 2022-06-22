# Pencil_Sketch : ASCII Art Generator

ASCII(American Standard Code for Information Interchange) is a common encoding format used for representing strings and text data in computers.
But..what if we use this for something other than text?
How about images? Images on your terminal!

### Goal
Convert images(jpg/png) to ASCII encoded strings, that look like the image.

Here's an example : 

![](https://i.imgur.com/fJsEVJi.png)
Also how to convert Ascii images into pencil sketch.

![](https://i.imgur.com/kHs9GHS.png)

### Built With:
* Python3 Programming
* Windows
* VS Code
### How to Proceed
1.import some python library
 ```  $ pip install opencv-python
   $ pip install pillow
   $ pip install imageio
   import imageio.v2
   from scipy.ndimage import gaussian_filter
   ```
 2.converting normal image to Ascii image.
 3.Taking Ascii image as input and turn into Pencil sktech.
### Usage:
1.Clone the repo.

2.Adding some extra features like import gaussian_filter from scipy.ndimage and imageio.v2 to turn out from ascii to pencil sketch.

3.Use  the data and fonts to choose relevant folder directory.
[](https://)
Taking as input and output as
```
image = cv2.imread("./data/input_image.jpg")
output_image=cv2.imwrite('./data/sketch_bg_white.png', returned)
```
Execute the binary:



Open terminal and compile the files 

![](https://i.imgur.com/1tn6WnB.png)




### Acknowledgments
* ACM IIT Roorkee Student Chapter

### Resources
- [Wiki article on ASCII Art and Images.](https://en.wikipedia.org/wiki/ASCII_art#Types_and_styles)
- [How digital images are stored in a computer.](https://alekya3.medium.com/how-images-are-stored-in-a-computer-f364d11b4e93)
- https://python.plainenglish.io/convert-a-photo-to-pencil-sketch-using-python-in-12-lines-of-code-4346426256d4
- [Another one regarding digital images](
https://www.analyticsvidhya.com/blog/2021/03/grayscale-and-rgb-format-for-storing-images/)
- \[Chapter 3] - "Raster Images", Fundamentals of Computer Graphics, Fourth Edition by Steve Marschner & Peter Shirley.
