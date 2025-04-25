from rembg import remove
import io

async def remove_background_service(file):
    input_data = await file.read()
    output_data = remove(input_data)
    return io.BytesIO(output_data)
