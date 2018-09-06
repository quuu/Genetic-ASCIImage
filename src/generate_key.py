from PIL import Image

'''
possible chars for brightness
'''

ASCII_CHARS = ['.',',',':',';','+','*','?','S','$','#','@']
ASCII_CHARS = ASCII_CHARS[::-1]


def generate(path):
    image = None
    try:
        image = Image.open(path)
    except Exception:
        print("Unable to find image in", path)
        return

    '''
    resizing the image
    '''

    (old_width,old_height) = image.size
    aspect_ratio = float(old_height)/float(old_width)
    new_width = 100
    new_height=int(aspect_ratio * new_width)
    new_dimensions = (new_width,new_height)
    image = image.resize(new_dimensions)

    '''
    grey scale the image
    '''

    image = image.convert('L')

    '''
    converting the image into ASCII representation based on
    brightness value of the pixel
    '''

    initial_pixels = list(image.getdata())
    new_pixels = [ASCII_CHARS[pixel_value//25] for pixel_value in initial_pixels]
    pixels = ''.join(new_pixels)

    '''
    inserting \n's to the ASCII for new lines of pixels
    '''

    new_image = [pixels[index:index+new_width] for index in range(0,len(pixels),new_width)]
    image = '\n'.join(new_image)

    '''
    making sure the image is good
    '''
    print(image)

    '''
    uncomment this for actual implementation
    '''
    #return image


if __name__ == '__main__':
    import sys
    path = sys.argv[1]
    generate(path)
