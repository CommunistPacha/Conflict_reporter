from fastapi import FastAPI, Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from models import Base, ConflictReport
from pydantic import BaseModel
from datetime import date, time
from typing import Optional

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

class ConflictReportUpdate(BaseModel):
    date: Optional[date] | None = None
    gps_location: str | None = None
    conflict_time: Optional[time] | None = None
    place: str | None = None
    village: str | None = None
    section: str | None = None
    range: str | None = None
    division: str | None = None
    conflict_animal: str | None = None
    conflict_type: str | None = None
    distance_from_forest: float | None = None
    habitat: str | None = None
    prt_engagement: bool | None = None
    prt_members: str | None = None
    indirect_signs: bool | None = None
    ct_images: bool | None = None
    fd_approach: bool | None = None
    media_involved: bool | None = None
    description: str | None = None


@app.post("/reports/")

def create_report(report: ConflictReportUpdate, db: Session = Depends(get_db)):
    db_report = ConflictReport(**report.dict())
    db.add(db_report)
    db.commit()
    db.refresh(db_report)
    return db_report

@app.get("/reports/")

@app.get("/reports/{report_id}")
def get_report(report_id: int, db: Session = Depends(get_db)):
    report = db.query(ConflictReport).filter(ConflictReport.id == report_id).first()
    if report is None:
        return {"error": "Report not found"}
    return report


@app.get("/reports/")
def get_reports(db: Session = Depends(get_db)):
    reports = db.query(ConflictReport).all()
    return reports


@app.put("/reports/{report_id}")
def update_report(report_id: int, report: ConflictReportUpdate, db: Session = Depends(get_db)):
    db_report = db.query(ConflictReport).filter(ConflictReport.id == report_id).first()
    if db_report is None:
        return {"error": "Report not found"}

    for key, value in report.dict(exclude_unset=True).items():
        setattr(db_report, key, value)

    db.commit()
    db.refresh(db_report)
    return db_report

@app.delete("/reports/{report_id}")
def delete_report(report_id: int, db: Session = Depends(get_db)):
    report = db.query(ConflictReport).filter(ConflictReport.id == report_id).first()
    if report is None:
        return {"error": "Report not found"}
    
    db.delete(report)
    db.commit()
    return {"message": "Report deleted successfully"}

