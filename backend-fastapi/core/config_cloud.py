import cloudinary
import os
from dotenv import load_dotenv

load_dotenv()

def init_cloudinary():
    cloudinary.config( 
    cloud_name = os.getenv("CLOUDINARY_CLOUD_NAME"), 
    api_key = os.getenv("CLOUDINARY_API_KEY"), 
    api_secret = os.getenv("CLOUDINARY_API_KEY_SECRET"),
    secure=True
)