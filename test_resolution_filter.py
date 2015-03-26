import sys
import os

from image import MyImage as Image
from filters import ImageResolution

path_prefix = "/home/sami/Pictures/2015-Quality/data"

def main():
    if len(sys.argv) < 2:
        print "You must define a path to an image"
        sys.exit(1)

    path = sys.argv[1]

    real_path = os.path.join(path_prefix, path)
    image = Image.get_image_from_imagej_tiff(real_path)
    print image.get_spacing()

    task = ImageResolution(image)
    task.calculate_power_spectrum(show=False)
    #task.calculate_azimuthal_average(show=False)
    task.calculate_summed_power(show=False)
if __name__ == "__main__":
    main()
