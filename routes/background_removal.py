from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import StreamingResponse
from services.background_removal_service import remove_background_service

router = APIRouter()

@router.post("/remove-bg/")
async def remove_background(file: UploadFile = File(...)):
    try:
        output_data = await remove_background_service(file)
        return StreamingResponse(
            output_data, 
            media_type="image/png", 
            headers={"Content-Disposition": f"attachment; filename=removed_{file.filename}"}
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
