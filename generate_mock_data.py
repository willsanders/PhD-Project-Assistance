import numpy as np
from PIL import Image
import os

# Create mock data for testing the parallel image processing
def generate_mock_images(num_images, image_size=(256, 256), output_dir="mock_images"):
    os.makedirs(output_dir, exist_ok=True)
   
    image_a_paths = []
    image_b_paths = []
   
    for i in range(num_images):
        # Create random images for 'a' and 'b'
        image_a = np.random.rand(*image_size) * 255  # Random values scaled to [0, 255]
        image_b = np.random.rand(*image_size) * 255
       
        # Convert arrays to PIL Images and save
        image_a_path = os.path.join(output_dir, f"B00001_a_{i}.tiff")
        image_b_path = os.path.join(output_dir, f"B00001_b_{i}.tiff")
       
        Image.fromarray(image_a.astype(np.uint8)).save(image_a_path)
        Image.fromarray(image_b.astype(np.uint8)).save(image_b_path)
       
        image_a_paths.append(image_a_path)
        image_b_paths.append(image_b_path)
   
    return image_a_paths, image_b_paths

# Generate mock data for testing
num_images = 1000  # Number of mock images to create
image_a_paths, image_b_paths = generate_mock_images(num_images)

print("Mock images generated.")