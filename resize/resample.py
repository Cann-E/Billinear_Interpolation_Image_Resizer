from numpy import zeros, uint8
from resize.interpolation import interpolation

class resample:
    def resize(self, image, fx=None, fy=None, interpolation=None):
        """calls the appropriate funciton to resample an image based on the interpolation method
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        interpolation: method used for interpolation ('either bilinear or nearest_neighbor)
        returns a resized image based on the interpolation method
        """
        if interpolation == 'bilinear':
            return self.bilinear_interpolation(image, float(fx), float(fy))

        elif interpolation == 'nearest_neighbor':
            return self.nearest_neighbor(image, float(fx), float(fy))

    def nearest_neighbor(self, image, fx, fy):
        """resizes an image using nearest neighbor approximation for resampling
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        returns a resized image based on the nearest neighbor interpolation method
        """
        in_height, in_width = image.shape[:2]
        out_height = int(in_height * fy)
        out_width = int(in_width * fx)
        output = zeros((out_height, out_width), uint8)

        for y in range(out_height):
            for x in range(out_width):
                src_x = int(round(x / fx))
                src_y = int(round(y / fy))
                src_x = min(src_x, in_width - 1)
                src_y = min(src_y, in_height - 1)
                output[y][x] = image[src_y][src_x]

        return output

    def bilinear_interpolation(self, image, fx, fy):
    
        """resizes an image using bilinear interpolation approximation for resampling
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        returns a resized image based on the bilinear interpolation method

        Note: Do not write the code to perform interpolation between points in this file. 
        There is a file named interpolation.py, and two function definitions are provided
        linear_interpolation: Write your code to perform linear interpolation between two in this function
        bilinear_interpolation: Write your code to perform bilinear interpolation using four points in this functions. 
                                As bilinear interpolation essentially does linear interpolation three times, you could simply call the 
                                linear_interpolation function three times, with the correct parameters. 
        """
        interp = interpolation()
        in_height, in_width = image.shape[:2]
        out_height = int(in_height * fy)
        out_width = int(in_width * fx)

        if len(image.shape) == 3:
            chan = image.shape[2]
        else:
            chan = 1

        if chan == 1:
            output = zeros((out_height, out_width), uint8)
        else:
            output = zeros((out_height, out_width, chan), uint8)

        for y in range(out_height):
            for x in range(out_width):
                origin_x = x / fx
                origin_y = y / fy

                col0 = int(origin_x)
                row0 = int(origin_y)
                col1 = min(col0 + 1, in_width - 1)
                row1 = min(row0 + 1, in_height - 1)

                x_offset = origin_x - col0
                y_offset = origin_y - row0

                if chan== 1:
                    a = image[row0][col0]
                    b = image[row0][col1]
                    c = image[row1][col0]
                    d = image[row1][col1]
                    output[y][x] = int(interp.bilinear_interpolation(a, b, c ,d, x_offset, y_offset))
                else:
                    for k in range(chan):
                        a = image[row0][col0][c]
                        b = image[row0][col1][c]
                        c = image[row1][col0][c]
                        d = image[row1][col1][c]
                        val = interp.bilinear_interpolation(a, b, c, d, x_offset, y_offset)
                        output[y][x][k] = int(val)

        return output
