from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.db.database import get_db

router = APIRouter()

@router.get("/infrastructure")
def get_infrastructure(db: Session = Depends(get_db)):
    query = text("""
        SELECT 
            id, type, label, material, 
            depth_m, install_year, status,
            ST_AsGeoJSON(geom)::json as geometry
        FROM infrastructure
    """)
    results = db.execute(query).fetchall()
    
    features = []
    for row in results:
        features.append({
            "type": "Feature",
            "geometry": row.geometry,
            "properties": {
                "id": row.id,
                "type": row.type,
                "label": row.label,
                "material": row.material,
                "depth_m": row.depth_m,
                "install_year": row.install_year,
                "status": row.status
            }
        })
    
    return {"type": "FeatureCollection", "features": features}