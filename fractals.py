import numpy as np
import random as r

def generate():
    
    wr = r.randrange(800, 1440)
    hr = r.randrange(600, 1080)
    #w = int(input("Width of image: "))
    #h = int(input("Height of image: "))
    #fr = r.random()
    #gr = r.random()
    f = float(input("Enter a Imaginary number between 0-1 (ex. 0.75): "))
    g = float(input("Enter Real number between 0-1 (ex. 0.355): "))
    name_input = input("Name File: ")
    
    x_min, x_max = -2.0, 2.0
    y_min, y_max = -2.0, 2.0

    name = str(name_input) + '.pgm'
    c = complex(g, f)

    rr = np.arange(x_min, x_max, (x_max - x_min) / wr)
    ir = np.arange(y_min, y_max, (y_max - y_min) / hr)

    with open(name, 'w') as output:
        output.write(f"P2\n{wr} {hr}\n255\n")

        for im in ir:
            for rm in rr:
                z = complex(rm, im)
                n = 255
                while abs(z) < 10 and n >= 5:
                    z = z ** 2 + c
                    n -= 5

                # Ensure the pixel value is an integer between 0 and 255
                pixel_value = int(n) if n >= 0 else 0
                pixel_value = min(pixel_value, 255)
                output.write(f"{pixel_value} ")

            output.write("\n")

generate()
