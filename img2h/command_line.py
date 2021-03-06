import sys, math, colorsys
import click
from PIL import Image

@click.command()
@click.option('--threshold', default=127, help='Brightness value at which pixels will be on')
@click.option('--show-output/--no-show-output', default=False, help='Show output image')
@click.option('--invert/--no-invert', default=False, help='Invert output image')
@click.argument('image_file')

def convert(image_file, threshold, show_output, invert):
    """
    img2h will convert bitmaps to C/C++ headers with pixels represented
    as byte arrays.
    """
    im = Image.open(image_file)
    width, height = im.size
    columns = int(math.ceil(width / 8.0))
    width = int(width)
    height = int(height)

    name, ext = image_file.split('.')
    header = open(name + '.h', 'w')

    header.write("#ifndef " + name.upper() +"_H\n")
    header.write("#define " + name.upper() +"_H\n\n")
    header.write("// Original image: " + str(width) + "x" + str(height) +"\n")
    header.write("static const unsigned char " + name + "[] = {\n")

    for y in range(0, height):
        header.write("\t")

        for column in range(0, columns):
            header.write("0B")

            for bit in range(0, 8):
                x = column * 8 + bit
                char = "0"

                if x < width:
                    pixel = colorsys.rgb_to_hsv(*im.getpixel((x, y)))
                    if pixel[2] < threshold:
                        char = "1"

                if invert:
                    char = "1" if char == "0" else "0"

                header.write(char)
                if show_output:
                    sys.stdout.write(" " if char == "0" else "#")

            header.write(", ")
        header.write("\n")
        if show_output:
            sys.stdout.write("\n")

    header.write("};\n\n")
    header.write("#endif\n")

    header.close()

if __name__ == '__main__':
    convert()
