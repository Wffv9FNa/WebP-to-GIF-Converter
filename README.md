# WebP to GIF Converter

This script converts all WebP images in the current directory to GIF format using the Python Imaging Library (PIL).

## Prerequisites

- Python 3.x
- Pillow package

## Installation

1. Clone the repository: `git clone https://github.com/Wffv9FNa/WebP-to-GIF-Converter`
2. Install Pillow package: `pip install pillow`

## Usage

1. Navigate to the directory containing WebP files you want to convert to GIF.
2. Run the script: `python webp_to_gif.py`
3. The script will convert all WebP files in the directory to GIF and delete the original WebP files.

## Notes

- The converted GIFs will be saved with a disposal mode of 2, which means that the background of each frame will be cleared to its original color.
- The script removes the background info from the WebP files, if present, before converting them to GIF.
- The converted GIFs will have the same name as the original WebP files but with the `.gif` extension.
