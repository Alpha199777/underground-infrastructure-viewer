from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base
from geoalchemy2 import Geometry

Base = declarative_base()

class Infrastructure(Base):
    __tablename__ = "infrastructure"

    id = Column(Integer, primary_key=True)
    type = Column(String(50))
    label = Column(String(255))
    material = Column(String(100))
    depth_m = Column(Float)
    install_year = Column(Integer)
    status = Column(String(50))
    geom = Column(Geometry(geometry_type="GEOMETRY", srid=4326))