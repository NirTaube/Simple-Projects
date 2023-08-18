def extract_svg_content(svg_str):
    # Try to extract the content between the opening and closing SVG tags
    try:
        return svg_str.split("<svg")[1].split(">", 1)[1].rsplit("</svg>", 1)[0]
    except IndexError:
        return ""

def combine_svgs(file_one_path, file_two_path, output_path):
    with open(file_one_path, 'r') as f:
        file_one_svg = f.read()

    with open(file_two_path, 'r') as f:
        file_two_svg = f.read()

    # Extract the content of the SVGs using the refined method
    file_one_content = extract_svg_content(file_one_svg)
    file_two_content = extract_svg_content(file_two_svg)

    # Check if content extraction was successful
    if not file_one_content or not file_two_content:
        print("Error: Unable to extract content from one or both SVG files.")
        return

    # Combine the contents.
    combined_content = f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 200 100'>\n{file_one_content}\n{file_two_content}\n</svg>"

    with open(output_path, 'w') as f:
        f.write(combined_content)

# Prompt the user for the paths to the SVG files and the output path
file_one_path = input("Enter the path to File one SVG: ")
file_two_path = input("Enter the path to File two SVG: ")
output_path = input("Enter the path where the combined SVG should be saved: ")

combine_svgs(file_one_path, file_two_path, output_path)
