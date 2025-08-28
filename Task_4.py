from PIL import Image

def edit_image():
    try:
        # Load the image
        image_path = input("Enter the path to your image: ")
        img = Image.open(image_path)
        
        # Convert to RGB if not already
        if img.mode != 'RGB':
            img = img.convert('RGB')
        
        width, height = img.size
        quarter_width = width // 4
        
        # Create a black rectangle for the left quarter
        black_rect = Image.new('RGB', (quarter_width, height), (0, 0, 0))
        
        # Create the right part of the original image
        right_part = img.crop((quarter_width, 0, width, height))
        
        # Combine the black rectangle and right part
        new_img = Image.new('RGB', (width, height))
        new_img.paste(black_rect, (0, 0))
        new_img.paste(right_part, (quarter_width, 0))
        
        # Save the modified image
        output_path = input("Enter the output path (e.g., modified_image.jpg): ")
        new_img.save(output_path)
        print(f"Image saved successfully to {output_path}")
        
    except FileNotFoundError:
        print("Image file not found. Please check the path.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the image editor
edit_image()