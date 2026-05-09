from PIL import Image

# ASCII characters from dark → light (this is the secret sauce)
ASCII_CHARS = "@%#*+=-:. "

def resize(image, new_width=100):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio * 0.55)
    return image.resize((new_width, new_height))

def grayscale(image):
    return image.convert("L")

def pixels_to_ascii(image):
    pixels = image.getdata()
    chars = "".join(ASCII_CHARS[pixel // 25] for pixel in pixels)
    return chars

def main(path):
    image = Image.open(path)

    image = resize(image)
    image = grayscale(image)

    ascii_str = pixels_to_ascii(image)

    width = image.width
    ascii_img = "\n".join(ascii_str[i:i+width] for i in range(0, len(ascii_str), width))

    with open("ascii_output.txt", "w") as f:
        f.write(ascii_img)

    print("Done! Check ascii_output.txt")

main("cat.png")