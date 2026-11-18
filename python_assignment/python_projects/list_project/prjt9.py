#*****************  Image Pixel Transformer (Grayscale & Threshold)  ******************

from functools import reduce

img = [
    [(255, 0, 0), (0, 255, 0), (0, 0, 255)],
    [(100, 100, 100), (200, 200, 200), (50, 50, 50)],
    [(255, 255, 255), (30, 30, 30), (150, 150, 150)]
]

gray = []

for row in img:
    g = list(map(lambda p: int(0.299*p[0] + 0.587*p[1] + 0.114*p[2]), row))
    gray.append(g)

print("Grayscale Image:")

for row in gray:
    for p in row:
        print(p, end=" ")
    print()

pixels = [p for row in gray for p in row]

dark = list(filter(lambda x: x < 128, pixels))

avg = reduce(lambda x, y: x + y, pixels) / len(pixels)

print("Dark Pixels:", len(dark))
print("Average Brightness:", round(avg, 2))

binary = list(map(lambda row: list(map(lambda x: 255 if x >= 128 else 0, row)), gray))

print("Binary Image:")

for row in binary:
    for p in row:
        if p == 255:
            print("1", end=" ")
        else:
            print("0", end=" ")
    print()

print("ASCII Image:")

for row in binary:
    for p in row:
        if p == 255:
            print("#", end=" ")
        else:
            print(".", end=" ")
    print()