from PIL import Image
import matplotlib.pyplot as plt


 

WIDTH = 400

HEIGHT = 300

IMG = Image('RGB', (WIDTH, HEIGHT))

PIXELS = IMG.pixels()

GRAD = plt.get_cmap('prism')

 

# Place origin at center of screen, then shift by x_SHIFT, y_SHIFT

X_SHIFT = 0

Y_SHIFT = 0

ZOOM = 1.0

 

MAX_ITERATIONS = 256

THRESHOLD = 2.0

 

def update_pixel_map():

 

    #c = 0.37+0.16j # The Serpent

    #c = -1 # The Basilica

    #c = -0.123+0.745j # The Douady Rabbit

    #c = -0.7709787-0.08545j # Crazy Spirals

    c = 0+1j # Lightning

 

    for x in range(WIDTH):

        for y in range(HEIGHT):

            #Convert pixel to a complex number z

            re = 1.5*(x-WIDTH/2)/(0.5*ZOOM*WIDTH)+X_SHIFT

            im = (y-HEIGHT/2)/(0.5*ZOOM*HEIGHT)+Y_SHIFT

            z = complex(re,im)

 

            level = 0

            # Iterate until orbit leaves THRESHOLD disk

            while(level < MAX_ITERATIONS):

                z = z**2+c

                if(abs(z)>THRESHOLD): break

                level += 1

 

            val = level/MAX_ITERATIONS # Should be between 0 and 1

            raw_rgb = GRAD.__call__(val)[0:3]

            rgb = [int(255*v) for v in raw_rgb]

            if(val == 1): rgb=[0,0,0]

            PIXELS[x,y] = tuple(rgb)

 

update_pixel_map()

IMG.save("julia.png")