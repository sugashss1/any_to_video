import os
from PIL import Image
import numpy as np
import math
def colored_image_to_binary(image_path):
    """Convert a colored image back to binary data."""
    with Image.open(image_path) as img:
        pixel_array = np.array(img)
        binary_data = pixel_array.tobytes()
    return binary_data
def binary_to_document(binary_data, output_file_path):
    #if not output_file_path.endswith(('.pdf', '.docx')):  # add more extensions as needed
        #output_file_path += '\\reconstructed.pdf'  # default to PDF format
    """Convert binary data back to a document."""
    with open(output_file_path, 'wb') as file:
        file.write(binary_data)
    print(f"Document saved as {output_file_path}")
binary_image_path = input('bin img path:')
reconstructed_doc_path = input('Reconstructed doc path:')
reconstructed_binary = colored_image_to_binary(binary_image_path)
binary_to_document(reconstructed_binary, reconstructed_doc_path)