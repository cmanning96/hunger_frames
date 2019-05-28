from moviepy.editor import *
from shutil import copyfile
from blueifier import blueify

def main():
  source_file = VideoFileClip("source.mp4")
  overlays = get_overlay_images()
  final_video = CompositeVideoClip([source_file] + overlays)
  final_video.write_videofile("output.mp4")

def get_overlay_images():
  copyfile("images/image4.png", "images/image4_copy.png")
  main_pos = (680, 220)
  main_size = (100, 250)
  alt_pos = (748, 15)
  alt_size = (70, 175)
  image_dict = {
    "images/image1.png": (16.2, 3.0, main_pos, main_size),
    "images/image2.png": (19.9, 0.85, main_pos, main_size),
    "images/image3.png": (23.5, 1.1, alt_pos, alt_size),
    "images/image4.png": (25.2, 0.9, alt_pos, alt_size),
    "images/image4_copy.png": (26.1, 2.5, main_pos, main_size),
    "images/image5.png": (28.9, 4.1, main_pos, main_size),
    "images/image6.png": (33.3, 4.3, main_pos, main_size)
  }
  # os.remove("images/image4_copy.png") 
  overlays = []
  for image_name in list(image_dict.keys()):
    start, duration, pos, size = image_dict[image_name]
    w, h = size
    img = ImageClip(image_name).set_start(start).set_duration(duration).resize(height=h, width=w).set_position(pos)
    overlays.append(img)
  return overlays

main()