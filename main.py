from fastapi import FastAPI, Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from models import Base, ConflictReport
from pydantic import BaseModel
from datetime import date, time

app = FastAPI()

DATABASE_URL = "sqlite:///./test.db"  #example db url
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class ConflictReportCreate(BaseModel):
    date: date
    gps_location: str
    conflict_time: time
    place: str
    village: str
    section: str
    range: str
    division: str
    conflict_animal: str
    conflict_type: str
    distance_from_forest: float
    habitat: str
    prt_engagement: bool
    prt_members: str
    indirect_signs: bool
    ct_images: bool
    fd_approach: bool
    media_involved: bool
    description: str

@app.post("/reports/")

def create_report(report: ConflictReportCreate, db: Session = Depends(get_db)):
    db_report = ConflictReport(**report.dict())
    db.add(db_report)
    db.commit()
    db.refresh(db_report)
    return db_report

@app.get("/reports/")

def get_reports(db: Session = Depends(get_db)):
    return db.query(ConflictReport).all()

@app.get("/")
def read_root():
    return {"message": "Conflict Reporter API is running"}



