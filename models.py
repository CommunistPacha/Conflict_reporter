from sqlalchemy import Column, Integer, String, Float, Boolean, Text, Date, Time
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ConflictReport(Base):
    __tablename__ = 'conflict_reports'
    
    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date)
    gps_location = Column(String)
    conflict_time = Column(Time)
    place = Column(String)
    village = Column(String)
    section = Column(String)
    range = Column(String)
    division = Column(String)
    conflict_animal = Column(String)
    conflict_type = Column(String)
    distance_from_forest = Column(Float)
    habitat = Column(String)
    prt_engagement = Column(Boolean)
    prt_members = Column(String)
    indirect_signs = Column(Boolean)
    ct_images = Column(Boolean)
    fd_approach = Column(Boolean)
    media_involved = Column(Boolean)
    description = Column(Text)
