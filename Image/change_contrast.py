#changing constrast for an image
from PIL import Image

def changeConstrast(img: Image, level: int) -> Image:
    factor = (259 * (level + 255)) / (255 * (259 - level))

    def constrast(c: int) -> int:
        """
            Fundamental transformation that will be performed on each and every bit.
        """
        return int(128 + factor * (c - 128))
    return img.point(constrast)

if __name__ == "__main__":
    with Image.open("file_path") as img:
        bright_img = changeConstrast(img, 170)
        bright_img.save('file_name.png', format="png")
