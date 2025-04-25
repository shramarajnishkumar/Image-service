from majormode.photoidmagick import BiometricPassportPhoto
import tempfile
from PIL import Image
import io
import os
from utils.file_validation import validate_passport_crop_file_extension

async def crop_passport_photo_service(file, width, height):
    # Validate file extension
    ext = os.path.splitext(file.filename)[1].lower().replace('.', '')
    if not validate_passport_crop_file_extension(ext):
        raise ValueError(f"Unsupported file type: .{ext}")
    
    pil_format = ext.upper() if ext.upper() in Image.registered_extensions().values() else 'JPEG'
    
    # Save the uploaded image temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=f".{ext}") as temp_file:
        temp_file.write(await file.read())
        temp_file_path = temp_file.name

    try:
        photo = BiometricPassportPhoto.from_file(
            image_file_path_name=temp_file_path,
            forbid_oblique_face=False,
            forbid_unevenly_open_eye=False,
            threshold_face_features_perpendicularity=0.15
        )
        cropped_image = photo.build_image(size=(width, height))

        buf = io.BytesIO()
        cropped_image.save(buf, format=pil_format)
        buf.seek(0)
        return buf
    except Exception as e:
        raise ValueError(f"Error cropping passport photo: {str(e)}")
    finally:
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)
