from PIL import Image

def image_to_binary(path, width=100):
    img = Image.open(path).convert("L")  # grayscale

    # resize for better output
    aspect_ratio = img.height / img.width
    height = int(width * aspect_ratio * 0.5)
    img = img.resize((width, height))

    pixels = img.getdata()

    # convert pixels to 0/1
    binary_str = ""
    for pixel in pixels:
        if pixel < 128:
            binary_str += "1"
        else:
            binary_str += "0"

    # format into lines
    binary_image = "\n".join(
        binary_str[i:i+width] for i in range(0, len(binary_str), width)
    )

    with open("binary_output.txt", "w") as f:
        f.write(binary_image)

    print("Done! Check binary_output.txt")

image_to_binary("cat.png")