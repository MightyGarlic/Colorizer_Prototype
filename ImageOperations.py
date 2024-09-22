from PIL import Image
import os

def list_filenames(folder_path):
    return [os.path.join(folder_path, f) for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

def rotate_and_save_image(input_image: str):
    image = Image.open(input_image)
    width, height  = image.size
    aspect_ratio = width / height
    
    if aspect_ratio > 1: 
        rotated_image = image.rotate(90, expand=True)
        if rotated_image.mode != 'RGB':  
            rotated_image = rotated_image.convert('RGB')
        rotated_image.save(input_image)

def convert_to_greyscale(input_filename, output_filename):
    img = Image.open(input_filename).convert('L')
    img.save(output_filename)