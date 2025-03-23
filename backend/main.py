from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Tuple

app = FastAPI()

# Aktivera CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CoordinateRequest(BaseModel):
    latitude: float
    longitude: float
    input_format: str

def decimal_to_dms(decimal: float) -> Tuple[int, int, float]:
    degrees = int(decimal)
    minutes_decimal = (decimal - degrees) * 60
    minutes = int(minutes_decimal)
    seconds = (minutes_decimal - minutes) * 60
    return degrees, minutes, seconds

def dms_to_decimal(degrees: int, minutes: int, seconds: float) -> float:
    return degrees + minutes/60 + seconds/3600

@app.post("/convert")
async def convert_coordinates(request: CoordinateRequest):
    try:
        if request.input_format == "decimal":
            # Konvertera till DMS
            lat_deg, lat_min, lat_sec = decimal_to_dms(request.latitude)
            lon_deg, lon_min, lon_sec = decimal_to_dms(request.longitude)
            
            return {
                "latitude": {
                    "degrees": lat_deg,
                    "minutes": lat_min,
                    "seconds": round(lat_sec, 2)
                },
                "longitude": {
                    "degrees": lon_deg,
                    "minutes": lon_min,
                    "seconds": round(lon_sec, 2)
                }
            }
        else:
            # Konvertera till decimalgrader
            return {
                "latitude": round(request.latitude, 6),
                "longitude": round(request.longitude, 6)
            }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 