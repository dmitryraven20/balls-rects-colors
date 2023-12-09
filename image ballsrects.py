import numpy as np
import matplotlib.pyplot as plt
from skimage.color import rgb2hsv
from skimage.measure import label, regionprops

def group_colors(color):
    result = []
    while color:
        color1 = color.pop(0)
        result.append([color1])
        for color2 in color.copy():
            if abs(color1 - color2) < 0.1:
                result[-1].append(color2)
                color.pop(color.index(color2))
    return result

def region_append(array1,array2):
    array1.extend('1')
    x,y = region.centroid_local
    array2.append(hue_values[int(x),int(y)])

image = plt.imread("balls_and_rects.png")
hsv = rgb2hsv(image)
h = hsv[:, :, 0]

image = image.mean(2)
image = image > 0
labeled = label(image)

labeled_regions = regionprops(labeled)
rects = []
circles = []
rectcol_list = []
circcol_list = []

for region in labeled_regions:
    bbox = region.bbox
    region_image = region.image

    hue_values = h[bbox[0]:bbox[2], bbox[1]:bbox[3]]

    if region.area == region.area_bbox:
        region_append(rects,rectcol_list)

    else:
        region_append(circles,circcol_list)

print(f"Всего: {np.max(labeled)}")

print(f"\n Прямоугольники: {len(rects)}")
for group in group_colors(rectcol_list):
    print(f"{np.average(group)}: {len(group)}")

print(f"\n Круги: {len(circles)}")
for group in group_colors(circcol_list):
    print(f"{np.average(group)}: {len(group)}")