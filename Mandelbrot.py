from PIL import Image
import math
import time

def colorAlgorithm(iters, maxIters):
    return round(255 / (maxIters - (n)))


if __name__ == "__main__":

    width, height, zoom = 1280, 720, 1
    bitmap = Image.new("RGB", (width, height), "white")
    pixels = bitmap.load()
    
    minRe = -2.0
    maxRe = 2
    minIm = -0.9

    maxIm = minIm + (maxRe - minRe) * height / width

    Re_factor = (maxRe - minRe) / (width - 1)
    Im_factor = (maxIm - minIm) / (height - 1)
    maxIters = 30

    start = time.time()

    for y in range(height):
        c_im = maxIm - y * Im_factor
        for x in range(width):
            c_re = minRe + x * Re_factor
            Z_re = c_re
            Z_im = c_im

            isInside = True
            for n in range(maxIters):
                s_Z_re = Z_re**2
                s_Z_im = Z_im**2
                if s_Z_im + s_Z_re > 4:
                    isInside = False
                    color = colorAlgorithm(n, maxIters)
                    pixels[x, y] = (0, color, round(color/2))
                    break
                Z_im = 2 * Z_re * Z_im + c_im
                Z_re = s_Z_re - s_Z_im + c_re
            
            if isInside == True:
                pixels[x, y] = (0, 0, 0)
    
    bitmap.show()

    end = time.time()
    print(end - start)

    