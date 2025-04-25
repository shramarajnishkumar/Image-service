SUPPORTED_EXTENSIONS = {
    "eps", "gif", "j2k", "j2p", "jp2", "jpx", "jpeg", "jpg", "jpe", "im", "icns", "msp", "pcx", "png", "pbm", "pgm", "ppm", "sgi", "spi", "tga", "tif", "tiff", "webp", "bmp", "dib", "ico", "xbm"
}

PASSPORT_SIZE_CROP_EXTENSIONS = {"jpg", "jpeg", "png"}

def validate_file_extension(ext: str) -> bool:
    return ext in SUPPORTED_EXTENSIONS

def validate_passport_crop_file_extension(ext: str) -> bool:
    return ext in PASSPORT_SIZE_CROP_EXTENSIONS 
