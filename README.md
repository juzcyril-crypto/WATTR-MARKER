# WATTR-MARKER
Watermarker created for Code in Place 2026

Automated orientation-aware batch watermarking tool for professional photography workflows.

## Folder Structure
Create a main folder named `WATTR MARKER`. Inside, create the following subfolders. **Note:** Do not include the forward slash (/) in the folder names.

* `input` (Folder: Place your raw photos here)
* `output` (Folder: The script will place your branded photos here)
* `watermarks` (Folder: Place your watermark files here)
    * `landscape_wm.png`
    * `portrait_wm.png`
* `watermarker.py` (The Python script)

## Setup Instructions
1. Open your terminal in the `WATTR MARKER` folder.
2. Create the virtual environment (sandbox):
   `python -m venv .venv`
3. Allow script execution for this session:
   `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process`
4. Activate the virtual environment:
   `.venv\Scripts\Activate.ps1`
5. Install the required image processing library:
   `pip install Pillow`

## How to Run
1. Ensure your watermark files are in the `watermarks` folder.
2. Place your source images into the `input` folder.
3. Run the script from the terminal:
   `python watermarker.py`
4. Your watermarked images will appear in the `output` folder.

## Technical Logic
* **EXIF Transpose:** Uses `ImageOps.exif_transpose` to automatically correct image orientation based on camera metadata.
* **Orientation Detection:** Uses conditional logic to detect if the photo is landscape or portrait.
* **Proportional Scaling:** Resizes the watermark strip to match the photo width exactly while maintaining the watermark's original aspect ratio.
* **Composition:** Pastes the watermark strip at the bottom edge and saves the result as a high-quality JPEG.
