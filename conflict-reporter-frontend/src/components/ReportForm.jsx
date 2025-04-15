import React, { useState } from "react";
import '../App.css';

const ReportForm = () => {
  const [formData, setFormData] = useState({
    date: "",
    gps_location: "",
    conflict_time: "",
    place: "",
    village: "",
    section: "",
    range: "",
    division: "",
    conflict_animal: "",
    conflict_type: "",
    distance_from_forest: "",
    habitat: "",
    prt_engagement: false,
    prt_members: "",
    indirect_signs: false,
    ct_images: false,
    fd_approach: false,
    media_involved: false,
    description: "",
  });

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    setFormData({
      ...formData,
      [name]: type === "checkbox" ? checked : value,
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    fetch("http://127.0.0.1:8000/reports/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(formData),
    })
      .then((response) => response.json())
      .then((data) => {
        console.log("Success:", data);
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  };

  return (
    <div className="form-container">
      <h2>Conflict Report Form</h2>
      <form onSubmit={handleSubmit} className="report-form">
        <div className="form-group">
          <label>Date</label>
          <input
            type="date"
            name="date"
            value={formData.date}
            onChange={handleChange}
            required
          />
        </div>

        <div className="form-group">
          <label>GPS Location</label>
          <input
            type="text"
            name="gps_location"
            value={formData.gps_location}
            onChange={handleChange}
            required
          />
        </div>

        <div className="form-group">
          <label>Conflict Time</label>
          <input
            type="time"
            name="conflict_time"
            value={formData.conflict_time}
            onChange={handleChange}
            required
          />
        </div>

        <div className="form-group">
          <label>Place</label>
          <input
            type="text"
            name="place"
            value={formData.place}
            onChange={handleChange}
            required
          />
        </div>

        <div className="form-group">
          <label>Village</label>
          <input
            type="text"
            name="village"
            value={formData.village}
            onChange={handleChange}
            required
          />
        </div>

        <div className="form-group">
          <label>Section</label>
          <input
            type="text"
            name="section"
            value={formData.section}
            onChange={handleChange}
            required
          />
        </div>

        <div className="form-group">
          <label>Range</label>
          <input
            type="text"
            name="range"
            value={formData.range}
            onChange={handleChange}
            required
          />
        </div>

        <div className="form-group">
          <label>Division</label>
          <input
            type="text"
            name="division"
            value={formData.division}
            onChange={handleChange}
            required
          />
        </div>

        <div className="form-group">
          <label>Conflict Animal</label>
          <input
            type="text"
            name="conflict_animal"
            value={formData.conflict_animal}
            onChange={handleChange}
            required
          />
        </div>

        <div className="form-group">
          <label>Conflict Type</label>
          <input
            type="text"
            name="conflict_type"
            value={formData.conflict_type}
            onChange={handleChange}
            required
          />
        </div>

        <div className="form-group">
          <label>Distance from Forest (km)</label>
          <input
            type="number"
            name="distance_from_forest"
            value={formData.distance_from_forest}
            onChange={handleChange}
            required
          />
        </div>

        <div className="form-group">
          <label>Habitat</label>
          <input
            type="text"
            name="habitat"
            value={formData.habitat}
            onChange={handleChange}
            required
          />
        </div>

        <div className="form-group checkbox-group">
          <label>PRT Engagement</label>
          <input
            type="checkbox"
            name="prt_engagement"
            checked={formData.prt_engagement}
            onChange={handleChange}
          />
        </div>

        <div className="form-group">
          <label>PRT Members</label>
          <input
            type="text"
            name="prt_members"
            value={formData.prt_members}
            onChange={handleChange}
          />
        </div>

        <div className="form-group checkbox-group">
          <label>Indirect Signs</label>
          <input
            type="checkbox"
            name="indirect_signs"
            checked={formData.indirect_signs}
            onChange={handleChange}
          />
        </div>

        <div className="form-group checkbox-group">
          <label>CT Images</label>
          <input
            type="checkbox"
            name="ct_images"
            checked={formData.ct_images}
            onChange={handleChange}
          />
        </div>

        <div className="form-group checkbox-group">
          <label>FD Approach</label>
          <input
            type="checkbox"
            name="fd_approach"
            checked={formData.fd_approach}
            onChange={handleChange}
          />
        </div>

        <div className="form-group checkbox-group">
          <label>Media Involved</label>
          <input
            type="checkbox"
            name="media_involved"
            checked={formData.media_involved}
            onChange={handleChange}
          />
        </div>

        <div className="form-group">
          <label>Description</label>
          <textarea
            name="description"
            value={formData.description}
            onChange={handleChange}
            required
          />
        </div>

        <button type="submit" className="submit-btn">Submit Report</button>
      </form>
    </div>
  );
};

export default ReportForm;
