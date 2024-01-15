import os
from PIL import Image
from colorama import init, Fore, Style

# Initialize colorama
init()

# Get a list of all WebP files in the current directory
webp_files = [f for f in os.listdir(".") if f.endswith(".webp")]

# Loop through each WebP file and convert it to GIF
for webp_file in webp_files:
    # Open the WebP file
    img = Image.open(webp_file)

    # Remove the background info if present
    img.info.pop("background", None)

    # Save the file as GIF with disposal mode 2
    gif_file = os.path.splitext(webp_file)[0] + ".gif"
    img.save(gif_file, save_all=True, disposal=2)

    # Delete the original WebP file
    os.remove(webp_file)

    # Print output message with original file name in yellow and new file name in cyan
    print(
        Fore.YELLOW
        + f"{webp_file}"
        + Style.RESET_ALL
        + " converted to "
        + Fore.CYAN
        + f"{gif_file}"
        + Style.RESET_ALL
    )
