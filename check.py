import sys
from PIL import Image

def classify(path):
    img = Image.open(path).convert("RGB")
    pixels = list(img.getdata())
    red = sum(1 for r, g, b in pixels if r > 150 and g < 100 and b < 100)
    return "DEFECT" if red / len(pixels) > 0.05 else "OK"

print(classify(sys.argv[1]))
