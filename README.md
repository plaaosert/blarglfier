# blarglfier
program written for a friend that blarglfies a folder of images

## how to use
- put files you want to blarglify into the `imgs/` folder
  - (clear the `output/` folder)
- run `main.py`
- look in `output/` for the results

## what is blarglification
blarglify in four easy steps:
- resize the image to 64x64, ignoring original aspect ratio and using nearest neighbour
- hue shift the image randomly
- jack up the contrast by a bunch
- resize the image back to 250x250 using nearest neighbour
- add scanlines by modifying the brightness according to a sin wave

## damn those faces look crazy howd you get them
thispersondoesnotexist
