from PIL import Image
import numpy as np
import math
import cv2
def to_binary(file_path):
    with open(file_path, 'rb') as file:
        return file.read()
def binary_to_colored_image(binary_data, output_image_path):
    """Convert binary data to a colored image."""
    # Calculate the image dimensions
    height = 480
    width = 640
    total_pixels=height*width
    data_len = len(binary_data)
    no_photos=math.ceil(data_len/(height*width*3))
    #pixel_array=list(np.empty(shape=no_photos))
    # Create a numpy array from the binary data, padding if necessary
    padding = height*width*3*no_photos - data_len
    padded_data = binary_data + b'\0' * padding
    four = cv2.VideoWriter_fourcc(*"FFV1")
    fps = 25
    out = cv2.VideoWriter('output.mkv',four, fps, (width, height))
    for i in range(0,no_photos):
        pixel_array = np.frombuffer(padded_data[i*total_pixels*3:total_pixels*3+i*total_pixels*3], dtype=np.uint8).reshape((height, width, 3))
        # Create and save the image
        img = Image.fromarray(pixel_array)
        out.write(pixel_array)
        img.save("v/"+output_image_path+str(i)+".png")
        print(f"Image saved as {output_image_path+str(i)}")
    out.release()

original_doc_path = input('Enter org path:')
binary_image_path = input('bin img path:')
binary_data = to_binary(original_doc_path)
img = binary_to_colored_image(binary_data, binary_image_path)