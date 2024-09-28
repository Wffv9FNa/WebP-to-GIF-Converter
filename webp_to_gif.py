import os
from PIL import Image
from colorama import init, Fore, Style


def convert_webp_to_gif(directory="."):
    # Initialize colorama
    init(autoreset=True)

    # Get a list of all WebP files in the specified directory
    webp_files = [f for f in os.listdir(directory) if f.endswith(".webp")]

    # Loop through each WebP file and convert it to GIF
    for webp_file in webp_files:
        webp_path = os.path.join(directory, webp_file)
        gif_path = os.path.splitext(webp_path)[0] + ".gif"

        # Open the WebP file
        with Image.open(webp_path) as img:
            # Remove the background info if present
            img.info.pop("background", None)
            # Save the file as GIF with disposal mode 2
            img.save(gif_path, save_all=True, disposal=2)

        # Delete the original WebP file
        os.remove(webp_path)

        # Print output message with original file name in yellow and new file name in cyan
        print_conversion_result(webp_path, gif_path)


def print_conversion_result(webp_file, gif_file):
    print(
        f"{Fore.YELLOW}{os.path.basename(webp_file)}{Style.RESET_ALL} "
        f"converted to {Fore.CYAN}{os.path.basename(gif_file)}{Style.RESET_ALL}"
    )


if __name__ == "__main__":
    convert_webp_to_gif()
