from PIL import Image
#import os

#def rename

def save_rgba_as_jpeg(image_path, save_path):
    try:
        with Image.open(image_path) as img:
            rgb_image = img.convert('RGB')
            rgb_image.save(save_path, 'JPEG')
    except Exception as e:
        print(f"An error occurred: {e}")



def remove_metadata(image_path, output_path):
  
    with Image.open(image_path) as img:
        data = img.getdata()

        new_img = Image.new(img.mode, img.size)
        new_img.putdata(data)

        # Save the image without metadata
        new_img.save(output_path, "JPEG")  
      

def scale(image_path, output_path, scale_factor: float = 0.8):

    original_image = Image.open(image_path)
    original_width, original_height = original_image.size

    new_width = int(original_width * scale_factor)
    new_height = int(original_height * scale_factor)

    resized_image = original_image.resize((new_width, new_height), Image.Resampling.LANCZOS)
    resized_image.save(output_path)

def remove_traces(image_path):
    save_rgba_as_jpeg(image_path, image_path)
    remove_metadata(image_path, image_path)
    scale(image_path, image_path, .8)


remove_traces("/Users/user/Downloads/1.jpeg")
