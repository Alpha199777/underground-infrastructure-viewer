# Underground Infrastructure Viewer

A full-stack Web GIS application for visualizing underground infrastructure networks.

## Tech Stack

- **Frontend:** MapLibre GL JS
- **Backend:** Python / FastAPI
- **Database:** PostgreSQL + PostGIS
- **Data Format:** GeoJSON
- **Version Control:** Git

## Project Structure

\\\
underground-infrastructure-viewer/
├── backend/          # FastAPI REST API server
│   ├── main.py       # Application entry point
│   └── requirements.txt
├── frontend/         # Map client application
│   └── index.html    # MapLibre GL JS map interface
├── data/             # GeoJSON geospatial datasets
├── docs/             # Sprint documentation
└── README.md
\\\

## Getting Started

### Backend
\\\ash
cd backend
python -m venv venv
venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn main:app --reload
\\\

API runs at: http://127.0.0.1:8000
API docs at: http://127.0.0.1:8000/docs

### Frontend
Open \rontend/index.html\ in your browser.

## Features
- Interactive dark-themed map centered on Geneva, Switzerland
- REST API with automatic documentation
- Clean frontend/backend separation
- Deployment-ready architecture

## Sprint Progress
- [x] Sprint 1 - Architecture and Project Setup
- [ ] Sprint 2 - Database and Geospatial Data
- [ ] Sprint 3 - API Geospatial Endpoints
- [ ] Sprint 4 - Map Layers and Feature Interaction
- [ ] Sprint 5 - Deployment
