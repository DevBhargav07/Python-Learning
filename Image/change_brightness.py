#we will try to change the brightness of an image
from PIL import Image

def changeBrightness(img: Image, level: float) -> Image:
    def bright(c: int) -> float:
        """
            Fundamental transformation that will be performed on each and every bit.
        """
        return 128 + level + (c -  128)
    if not -255.0 <= level <= 255:
        raise ValueError('Value must be in between -255.0 (Black) and 255.0 (White)')
    return img.point(bright)





if __name__ == "__main__":
    with Image.open("file_path") as img:
        bright_img = changeBrightness(img, 125)
        bright_img.save('file_name.png', format="png")
