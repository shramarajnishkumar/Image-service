from fastapi import APIRouter, UploadFile, File, Query, HTTPException
from fastapi.responses import StreamingResponse
from services.passport_photo_crop_service import crop_passport_photo_service

router = APIRouter()

@router.post("/crop-passport-photo/")
async def crop_passport_photo(
    file: UploadFile = File(...),
    width: int = Query(..., description="Width of the passport photo in pixels"),
    height: int = Query(..., description="Height of the passport photo in pixels")
):
    try:
        output_data = await crop_passport_photo_service(file, width, height)
        return StreamingResponse(
            output_data, 
            media_type="image/png", 
            headers={"Content-Disposition": f"attachment; filename=passport_{file.filename}"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
