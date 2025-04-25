from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import StreamingResponse
from services.auto_crop_service import auto_crop_image_service

router = APIRouter()

@router.post("/auto-crop-passport-size/")
async def auto_crop_image(file: UploadFile = File(...)):
    try:
        output_data = await auto_crop_image_service(file)
        return StreamingResponse(
            output_data, 
            media_type="image/png", 
            headers={"Content-Disposition": f"attachment; filename=cropped_{file.filename}"}
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
