
import os
from PIL import Image, ImageOps # Import ImageOps here

def apply_watermark(image_path, output_path):
    photo = Image.open(image_path)
    photo = ImageOps.exif_transpose(photo)
    photo = photo.convert("RGBA")
    w, h = photo.size
    
    # Check orientation with strict logic
    if w > h:
        wm_path = "watermarks/landscape_wm.png"
    else:
        wm_path = "watermarks/portrait_wm.png"
        
    print(f"DEBUG: Processing {os.path.basename(image_path)} | Size: {w}x{h} | Using: {wm_path}")

    watermark = Image.open(wm_path).convert("RGBA")

    # Resize watermark to full width
    target_wm_width = w
    aspect_ratio = watermark.height / watermark.width
    target_wm_height = int(target_wm_width * aspect_ratio)
    watermark = watermark.resize((target_wm_width, target_wm_height))

    pos = (0, h - target_wm_height)

    transparent = Image.new("RGBA", photo.size, (0, 0, 0, 0))
    transparent.paste(photo, (0, 0))
    transparent.paste(watermark, pos, mask=watermark)
    transparent.convert("RGB").save(output_path, "JPEG", quality=95)

# --- Batch Processing remains the same ---
input_dir = "input"
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

print("Starting batch watermarking...")
processed_count = 0

for filename in os.listdir(input_dir):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        try:
            apply_watermark(os.path.join(input_dir, filename), os.path.join(output_dir, filename))
            print(f"✅ Processed: {filename}")
            processed_count += 1
        except Exception as e:
            print(f"❌ Error processing {filename}: {e}")

print(f"\n--- Done! Processed {processed_count} images.")