import os
from PIL import Image

# 1. Define folder paths and desired size
input_folder = 'input_images'
output_folder = 'output_images'
new_size = (800, 800) # Resize images to fit within an 800x800 box

# 2. Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 3. Loop through all files in the input folder
for filename in os.listdir(input_folder):
    # Check if the file is a common image type
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
        try:
            # Construct full file paths
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            # Open the image
            with Image.open(input_path) as img:
                # Use thumbnail to resize while maintaining aspect ratio
                img.thumbnail(new_size)

                # Save the resized image to the output folder
                img.save(output_path)
                print(f'Resized and saved: {filename}')

        except Exception as e:
            print(f'Could not process {filename}: {e}')

print("\nImage resizing complete. Resized images are in the 'output_images' folder.")