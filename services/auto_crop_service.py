from autocrop import Cropper
import tempfile
from PIL import Image
import io
import os
import numpy as np
from utils.file_validation import validate_file_extension

async def auto_crop_image_service(file):
    # Validate file extension
    ext = os.path.splitext(file.filename)[1].lower().replace('.', '')
    if not validate_file_extension(ext):
        raise ValueError(f"Unsupported file type: .{ext}")
    
    # Save the uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=f".{ext}") as temp_file:
        temp_file.write(await file.read())
        temp_file_path = temp_file.name
    
    # Crop the image
    cropper = Cropper()
    cropped_array = cropper.crop(temp_file_path)

    if isinstance(cropped_array, np.ndarray) and cropped_array.size > 0:
        cropped_image = Image.fromarray(cropped_array)
        buf = io.BytesIO()
        cropped_image.save(buf, format="PNG")
        buf.seek(0)
        return buf
    else:
        raise ValueError("No face detected or unable to crop image")
