# Hirst Painting Extract RGB values from image
import colorgram

color_list = []
colors = colorgram.extract('image.jpg', 30)
print(colors)

for i in colors:
    # color_list.append(i.rgb)
    r = i.rgb.r
    g = i.rgb.g
    b = i.rgb.b
    color_tup = (r, g, b)
    color_list.append(color_tup)

print(color_list)

