from PIL import Image

def blueify(image_src):
  image = Image.open(image_src)
  new_image = image.copy()
  new_image = new_image.convert("RGBA")
  new_image.putalpha(1)
  w, h = image.width, image.height
  for x in range(w):
    for y in range(h):
      color = image.getpixel((x, y))
      blue_val = get_blue_value(color)
      new_image.putpixel((x, y), blue_val)
  return new_image

def get_blue_value(color):
  total = 0
  for index in [0, 1, 2]:
    total += color[index]
  blue_value = int(total/3)
  nulls, non_nulls = 0, 0
  # if blue_value > 240:
  #   return (0, 0, blue_value, 0)
  return (0, 0, blue_value, 1)