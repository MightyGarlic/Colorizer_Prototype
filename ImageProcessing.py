from ImageOperations import list_filenames, rotate_and_save_image, convert_to_greyscale
import os 

folder_path = os.path.expanduser('~/Machine Learning/Colorizer/training_data/Images to Process')
filenames = list_filenames(folder_path)

for file_name in os.listdir(folder_path):
    if "Zone.Identifier" in file_name:
        file_path = os.path.join(folder_path, file_name)
        os.remove(file_path) 

for file_name in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file_name)  # Get full path to the file
    ext = os.path.splitext(file_name)[1].lower()
    
    if ext in ['.jpg', '.png']:  # Check if it's a JPG or PNG
        rotate_and_save_image(file_path)


for input_filename in filenames:
    name, ext = input_filename.rsplit('.', 1)
    if (ext == 'jpg' or ext == 'png'):
      output_filename = f"{name}_greyscale.{ext}"
      if not os.path.exists(output_filename) and not 'greyscale' in input_filename:
            convert_to_greyscale(input_filename, output_filename)
