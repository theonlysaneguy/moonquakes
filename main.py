from fastapi import FastAPI
from fastapi.responses import JSONResponse
import csv
import os

app = FastAPI()

@app.post("/upload_csv/")
async def upload_csv():
    try:
        file_path = r"C:\1\new 5.csv"
        with open(file_path, "r") as file:
            csv_data = file.read()
        csv_rows = csv_data.split("\n")
        csv_reader = csv.DictReader(csv_rows)
        data = []
        for row in csv_reader:
            data.append({
                "Time stamp": row.get("Timestamp"),
                "Latitude": row.get("Lat"),
                "Longitude": row.get("Long"),
                "Seismic activity value": row.get("Magnitude"),
                "Moon quake type": row.get("Moonquake Type")
            })

        return JSONResponse(content={"status": "success", "filename": file_path, "data": data}, media_type="application/json")
    except Exception as e:
        return JSONResponse(content={"status": "error", "message": str(e)}, media_type="application/json")
