from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Tuple, List, Optional
import re

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
    coordinates: List[str]
    input_format: str

def decimal_to_dms(decimal: float) -> Tuple[int, int, float]:
    degrees = int(decimal)
    minutes_decimal = (decimal - degrees) * 60
    minutes = int(minutes_decimal)
    seconds = (minutes_decimal - minutes) * 60
    return degrees, minutes, seconds

def dms_to_decimal(degrees: int, minutes: int, seconds: float) -> float:
    return degrees + minutes/60 + seconds/3600

def parse_ddmmss_format(coord_str: str) -> Optional[Tuple[float, float]]:
    # Hantera format som ddmmssN dddmmssE
    pattern = r'(\d{2})(\d{2})(\d{2})([NS]),\s*(\d{3})(\d{2})(\d{2})([EW])'
    match = re.match(pattern, coord_str)
    if match:
        lat_d, lat_m, lat_s, lat_dir, lon_d, lon_m, lon_s, lon_dir = match.groups()
        lat = dms_to_decimal(int(lat_d), int(lat_m), int(lat_s))
        lon = dms_to_decimal(int(lon_d), int(lon_m), int(lon_s))
        if lat_dir == 'S': lat = -lat
        if lon_dir == 'W': lon = -lon
        return lat, lon
    return None

def parse_ddmm_format(coord_str: str) -> Optional[Tuple[float, float]]:
    # Hantera format som ddmmN dddmmE
    pattern = r'(\d{2})(\d{2})([NS]),\s*(\d{3})(\d{2})([EW])'
    match = re.match(pattern, coord_str)
    if match:
        lat_d, lat_m, lat_dir, lon_d, lon_m, lon_dir = match.groups()
        lat = dms_to_decimal(int(lat_d), int(lat_m), 0)
        lon = dms_to_decimal(int(lon_d), int(lon_m), 0)
        if lat_dir == 'S': lat = -lat
        if lon_dir == 'W': lon = -lon
        return lat, lon
    return None

def parse_dd_format(coord_str: str) -> Optional[Tuple[float, float]]:
    # Hantera format som ddN dddE
    pattern = r'(\d{2})([NS]),\s*(\d{3})([EW])'
    match = re.match(pattern, coord_str)
    if match:
        lat_d, lat_dir, lon_d, lon_dir = match.groups()
        lat = dms_to_decimal(int(lat_d), 0, 0)
        lon = dms_to_decimal(int(lon_d), 0, 0)
        if lat_dir == 'S': lat = -lat
        if lon_dir == 'W': lon = -lon
        return lat, lon
    return None

def parse_ddmmss_dot_format(coord_str: str) -> Optional[Tuple[float, float]]:
    # Hantera format som dd°mm'ss"N, ddd°mm'ss"W
    pattern = r'(\d{2})°(\d{2})\'(\d{2})\"([NS]),\s*(\d{3})°(\d{2})\'(\d{2})\"([EW])'
    match = re.match(pattern, coord_str)
    if match:
        lat_d, lat_m, lat_s, lat_dir, lon_d, lon_m, lon_s, lon_dir = match.groups()
        lat = dms_to_decimal(int(lat_d), int(lat_m), int(lat_s))
        lon = dms_to_decimal(int(lon_d), int(lon_m), int(lon_s))
        if lat_dir == 'S': lat = -lat
        if lon_dir == 'W': lon = -lon
        return lat, lon
    return None

def parse_ddmm_dot_format(coord_str: str) -> Optional[Tuple[float, float]]:
    # Hantera format som Ndd°mm.ii' Ed°mm.ii'
    pattern = r'N(\d{2})°(\d{2})\.(\d{2})\'\s+E(\d{3})°(\d{2})\.(\d{2})\''
    match = re.match(pattern, coord_str)
    if match:
        lat_d, lat_m, lat_i, lon_d, lon_m, lon_i = match.groups()
        lat = dms_to_decimal(int(lat_d), int(lat_m), int(lat_i))
        lon = dms_to_decimal(int(lon_d), int(lon_m), int(lon_i))
        return lat, lon
    return None

def parse_ddmmss_compact_format(coord_str: str) -> Optional[Tuple[float, float]]:
    # Hantera format som ddmmssN dddmmssE
    pattern = r'(\d{2})(\d{2})(\d{2})([NS])\s+(\d{3})(\d{2})(\d{2})([EW])'
    match = re.match(pattern, coord_str)
    if match:
        lat_d, lat_m, lat_s, lat_dir, lon_d, lon_m, lon_s, lon_dir = match.groups()
        lat = dms_to_decimal(int(lat_d), int(lat_m), int(lat_s))
        lon = dms_to_decimal(int(lon_d), int(lon_m), int(lon_s))
        if lat_dir == 'S': lat = -lat
        if lon_dir == 'W': lon = -lon
        return lat, lon
    return None

def parse_ddmm_compact_format(coord_str: str) -> Optional[Tuple[float, float]]:
    # Hantera format som ddmmN dddmmE
    pattern = r'(\d{2})(\d{2})([NS])\s+(\d{3})(\d{2})([EW])'
    match = re.match(pattern, coord_str)
    if match:
        lat_d, lat_m, lat_dir, lon_d, lon_m, lon_dir = match.groups()
        lat = dms_to_decimal(int(lat_d), int(lat_m), 0)
        lon = dms_to_decimal(int(lon_d), int(lon_m), 0)
        if lat_dir == 'S': lat = -lat
        if lon_dir == 'W': lon = -lon
        return lat, lon
    return None

def parse_dd_compact_format(coord_str: str) -> Optional[Tuple[float, float]]:
    # Hantera format som ddN dddE
    pattern = r'(\d{2})([NS])\s+(\d{3})([EW])'
    match = re.match(pattern, coord_str)
    if match:
        lat_d, lat_dir, lon_d, lon_dir = match.groups()
        lat = dms_to_decimal(int(lat_d), 0, 0)
        lon = dms_to_decimal(int(lon_d), 0, 0)
        if lat_dir == 'S': lat = -lat
        if lon_dir == 'W': lon = -lon
        return lat, lon
    return None

def parse_decimal_format(coord_str: str) -> Optional[Tuple[float, float]]:
    # Hantera format som -dd.jjjjj, dd.jjjjjj eller dd, dd
    pattern = r'(-?\d+(?:\.\d+)?),\s*(-?\d+(?:\.\d+)?)'
    match = re.match(pattern, coord_str)
    if match:
        lat, lon = map(float, match.groups())
        return lat, lon
    return None

def parse_ddmmss_space_format(coord_str: str) -> Optional[Tuple[float, float]]:
    # Hantera format som 593346N 0195859E eller 593346N0195859E
    pattern = r'(\d{2})(\d{2})(\d{2})([NS])\s*(\d{3})(\d{2})(\d{2})([EW])'
    match = re.match(pattern, coord_str)
    if match:
        lat_d, lat_m, lat_s, lat_dir, lon_d, lon_m, lon_s, lon_dir = match.groups()
        lat = dms_to_decimal(int(lat_d), int(lat_m), int(lat_s))
        lon = dms_to_decimal(int(lon_d), int(lon_m), int(lon_s))
        if lat_dir == 'S': lat = -lat
        if lon_dir == 'W': lon = -lon
        return lat, lon
    return None

def parse_coordinates(coord_str: str) -> Optional[Tuple[float, float]]:
    # Prova alla format i ordning
    parsers = [
        parse_decimal_format,
        parse_ddmmss_space_format,
        parse_ddmmss_format,
        parse_ddmm_format,
        parse_dd_format,
        parse_ddmmss_dot_format,
        parse_ddmm_dot_format,
        parse_ddmmss_compact_format,
        parse_ddmm_compact_format,
        parse_dd_compact_format
    ]
    
    for parser in parsers:
        result = parser(coord_str)
        if result:
            return result
    return None

@app.post("/convert")
async def convert_coordinates(request: CoordinateRequest):
    try:
        results = []
        print(f"Input format: {request.input_format}")
        for coord_str in request.coordinates:
            # Ta bort eventuella extra mellanslag i början och slutet
            coord_str = coord_str.strip()
            print(f"Processing coordinate: {coord_str}")
            parsed = parse_coordinates(coord_str)
            if parsed is None:
                raise ValueError(f"Kunde inte tolka koordinaterna: {coord_str}")
            
            lat, lon = parsed
            print(f"Parsed coordinates: lat={lat}, lon={lon}")
            
            if request.input_format == "dms":
                # Konvertera till DMS
                lat_deg, lat_min, lat_sec = decimal_to_dms(abs(lat))
                lon_deg, lon_min, lon_sec = decimal_to_dms(abs(lon))
                
                result = {
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
                print(f"DMS result: {result}")
                results.append(result)
            else:
                # Konvertera till decimalgrader
                result = {
                    "latitude": round(lat, 6),
                    "longitude": round(lon, 6)
                }
                print(f"Decimal result: {result}")
                results.append(result)
        return results
    except Exception as e:
        print(f"Error: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 