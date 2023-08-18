from PIL import Image

def combine_pngs(file_one_path, file_two_path, output_path, orientation="horizontal"):
    # Open the images
    img1 = Image.open(file_one_path)
    img2 = Image.open(file_two_path)
    
    # Combine the images based on the desired orientation
    if orientation == "horizontal":
        width = img1.width + img2.width
        height = max(img1.height, img2.height)
        combined_img = Image.new('RGBA', (width, height), (255, 255, 255, 0))  # RGBA mode for transparency
        combined_img.paste(img1, (0, 0), img1)
        combined_img.paste(img2, (img1.width, 0), img2)
    elif orientation == "vertical":
        width = max(img1.width, img2.width)
        height = img1.height + img2.height
        combined_img = Image.new('RGBA', (width, height), (255, 255, 255, 0))
        combined_img.paste(img1, (0, 0), img1)
        combined_img.paste(img2, (0, img1.height), img2)
    else:
        print("Invalid orientation choice. Choose either 'horizontal' or 'vertical'.")
        return

    # Save the combined image
    combined_img.save(output_path)

# Prompt the user for the paths to the PNG files, the output path, and the orientation
file_one_path = input("Enter the path to File one PNG: ")
file_two_path = input("Enter the path to File two PNG: ")
orientation = input("Enter orientation (horizontal for side-by-side or vertical for stacked): ").strip().lower()
output_path = input("Enter the path where the combined PNG should be saved: ")

combine_pngs(file_one_path, file_two_path, output_path, orientation)

