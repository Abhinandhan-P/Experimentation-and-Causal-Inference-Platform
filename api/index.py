import os
import sys
from pathlib import Path

# Add project root and src directory to Python path
ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR))
sys.path.insert(0, str(ROOT_DIR / "src"))

try:
    from src.api import app
except Exception as e:
    from fastapi import FastAPI
    from fastapi.responses import JSONResponse
    import traceback
    
    app = FastAPI()
    
    @app.get("/{full_path:path}")
    async def catch_all(full_path: str):
        return JSONResponse(
            status_code=500,
            content={
                "error": "Initialization Failed",
                "details": str(e),
                "traceback": traceback.format_exc()
            }
        )

