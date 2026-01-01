
import cv2
import numpy as np
from PIL import Image
import piexif
import hashlib

def compute_sha256(image_path):
    with open(image_path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

def compute_phash(image_path):
    img = Image.open(image_path).convert("L").resize((32, 32))
    pixels = np.array(img)
    dct = cv2.dct(np.float32(pixels))
    dct_low_freq = dct[:8, :8]
    median_val = np.median(dct_low_freq)
    phash_bits = (dct_low_freq > median_val).flatten()
    return ''.join(['1' if bit else '0' for bit in phash_bits])

def extract_exif(image_path):
    exif_data = piexif.load(image_path)
    return {
        "DateTime": exif_data["0th"].get(piexif.ImageIFD.DateTime, b"").decode(),
        "Make": exif_data["0th"].get(piexif.ImageIFD.Make, b"").decode(),
        "Model": exif_data["0th"].get(piexif.ImageIFD.Model, b"").decode()
    }

if __name__ == "__main__":
    image_path = "sample.jpg"
    print("SHA256:", compute_sha256(image_path))
    print("pHash:", compute_phash(image_path))
    print("EXIF:", extract_exif(image_path))
