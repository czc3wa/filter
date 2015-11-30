import pygame as pg

# grayPixel: pixel -> pixel
# compute and return a gray pixel with the same intensity
# as the given pixel
def grayPixel(pixel):
    red_intensity = pixel[0]
    green_intensity = pixel[1]
    blue_intensity = pixel[2]
    ave_intensity = (red_intensity + green_intensity+ blue_intensity)//3
    return (ave_intensity, ave_intensity, ave_intensity)

# channel: pixel -> channel -> pixel
# return a gray pixel with intensity from given channel of given pixel
def channel(pixel,chan):
    return (pixel[chan],pixel[chan],pixel[chan])


# inverse: pixel -> pixel
# return the color negative of the given pixel
def inverse(pixel):
    return (255-pixel[0], 255-pixel[1], 255-pixel[2])


# intensify: pixel -> nat255 -> pixel
# brighten each channel of pixel by quantity
def add_intensity(pixel):
    quantity = 10
    red_intensity = pixel[0]
    green_intensity = pixel[1]
    blue_intensity = pixel[2]
    if (pixel[0] > 245):
        red_intensity = pixel[0]
    else:
        red_intensity = pixel[0]+quantity
    if (pixel[1] > 245):
        green_intensity = pixel[1]
    else:
        green_intensity = pixel[1]+quantity
    if (pixel[2] > 245):
        blue_intensity = pixel[2]
    else:
        blue_intensity = pixel[2]+quantity
    return (red_intensity, green_intensity, blue_intensity)

def brighten_intensity(image_surf):

    # get pixel dimensions of image
    rows = image_surf.get_size()[0]
    cols = image_surf.get_size()[1]
    
    # get reference to and lock pixel array
    pixels3d = pg.surfarray.pixels3d(image_surf)

    # update pixels in place (side effect!)
    for x in range(rows):
        for y in range(cols):
            pixels3d[x,y] = add_intensity(pixels3d[x,y])
            

def sub_intensity(pixel):
    quantity = 10
    red_intensity = pixel[0]
    green_intensity = pixel[1]
    blue_intensity = pixel[2]
    if (pixel[0] < 10):
        red_intensity = pixel[0]
    else:
        red_intensity = pixel[0]-quantity
    if (pixel[1] < 10):
        green_intensity = pixel[1]
    else:
        green_intensity = pixel[1]-quantity
    if (pixel[2] < 10):
        blue_intensity = pixel[2]
    else:
        blue_intensity = pixel[2]-quantity
    return (red_intensity, green_intensity, blue_intensity)

def darken_intensity(image_surf):

    # get pixel dimensions of image
    rows = image_surf.get_size()[0]
    cols = image_surf.get_size()[1]
    
    # get reference to and lock pixel array
    pixels3d = pg.surfarray.pixels3d(image_surf)

    # update pixels in place (side effect!)
    for x in range(rows):
        for y in range(cols):
            pixels3d[x,y] = sub_intensity(pixels3d[x,y])
            



    

def invert(image_surf):

    # get pixel dimensions of image
    rows = image_surf.get_size()[0]
    cols = image_surf.get_size()[1]
    
    # get reference to and lock pixel array
    pixels3d = pg.surfarray.pixels3d(image_surf)

    # update pixels in place (side effect!)
    for x in range(rows):
        for y in range(cols):
            pixels3d[x,y] = inverse(pixels3d[x,y])

def bw(image_surf):

    # get pixel dimensions of image
    rows = image_surf.get_size()[0]
    cols = image_surf.get_size()[1]
    
    # get reference to and lock pixel array
    pixels3d = pg.surfarray.pixels3d(image_surf)

    # update pixels in place (side effect!)
    for x in range(rows):
        for y in range(cols):
            pixels3d[x,y] = grayPixel(pixels3d[x,y])
