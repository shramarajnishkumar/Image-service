from fastapi import FastAPI
from routes.background_removal import router as background_removal_router
from routes.auto_crop import router as auto_crop_router
from routes.passport_photo_crop import router as passport_photo_crop_router

app = FastAPI(
    title="Image Services APIs",
    summary="""
        Efficient and intelligent image processing endpoints including background removal, automatic facial cropping, and compliant biometric passport photo generation.
    """
)

# Include routers for different functionality
app.include_router(background_removal_router)
app.include_router(auto_crop_router)
app.include_router(passport_photo_crop_router)