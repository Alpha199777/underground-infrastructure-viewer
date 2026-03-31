# Underground Infrastructure Viewer

A full-stack Web GIS application for visualizing underground infrastructure networks in Geneva, Switzerland.

---

## 🚀 Live Demo

* **Frontend (Vercel)**: https://underground-infrastructure-viewer.vercel.app
* **Backend API (Railway)**: https://underground-infra-api-production.up.railway.app
* **API Docs**: https://underground-infra-api-production.up.railway.app/docs
* **Health Check**: https://underground-infra-api-production.up.railway.app/health

---

## 🧠 Project Overview

This project demonstrates a complete geospatial web architecture:

* Interactive infrastructure visualization on a web map
* Geospatial data served via a FastAPI REST API
* PostgreSQL/PostGIS-backed spatial data access
* Full production deployment (Vercel + Railway)

---

## 🏗️ Architecture

```text
Frontend (Vercel)
    ↓ HTTPS / JSON
Backend API (FastAPI - Railway)
    ↓ SQL
PostgreSQL + PostGIS
```

---

## 🛠️ Tech Stack

* **Frontend**: MapLibre GL JS
* **Backend**: Python / FastAPI
* **Database**: PostgreSQL + PostGIS
* **Data Format**: GeoJSON

### Deployment

* **Frontend**: Vercel
* **Backend**: Railway

---

## 📁 Project Structure

```text
underground-infrastructure-viewer/
│
├── backend/        # FastAPI REST API
│   ├── app/
│   ├── main.py
│   └── requirements.txt
│
├── frontend/       # Map client application
│   └── index.html
│
├── data/           # GeoJSON datasets
├── docs/           # Sprint documentation
│
├── Dockerfile
├── railway.toml
└── README.md
```

---

## ⚙️ Features

* Interactive dark-themed map centered on Geneva
* Multiple infrastructure layers:

  * Water pipes
  * Electrical cables
  * Telecom
  * Sewer
* GeoJSON FeatureCollection served by API
* Layer controls (toggle visibility)
* FastAPI automatic documentation
* Clean frontend/backend separation
* CORS configured via environment variables
* Health check endpoint (`/health`) with DB validation

---

## 🧪 API

### Endpoint

```http
GET /api/infrastructure
```

### Response format

```json
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "geometry": {},
      "properties": {
        "id": 1,
        "type": "water",
        "label": "Main pipe",
        "material": "PVC",
        "depth_m": 1.5,
        "install_year": 2012,
        "status": "active"
      }
    }
  ]
}
```

---

## 🧰 Local Development

### Backend

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

* API → http://127.0.0.1:8000
* Docs → http://127.0.0.1:8000/docs

---

### Frontend

```bash
cd frontend
python -m http.server 5500
```

Open in browser:

http://127.0.0.1:5500

---

## 🔐 Environment Variables

```env
DATABASE_URL=your_database_connection_string
ALLOWED_ORIGINS=http://127.0.0.1:5500,http://localhost:5500,https://underground-infrastructure-viewer.vercel.app
```

---

## 🚀 Deployment

### Backend (Railway)

* Dockerized FastAPI application
* Environment-based configuration
* Health check endpoint (`/health`)
* CORS controlled via `ALLOWED_ORIGINS`

### Frontend (Vercel)

* Static deployment
* Consumes Railway API
* No build step required

---

## 📈 Sprint Progress

* [x] Sprint 1 - Architecture and Project Setup
* [x] Sprint 2 - Database and Geospatial Data
* [x] Sprint 3 - Map Layers and Feature Integration
* [x] Sprint 4 - Polish and UI
* [x] Sprint 5 - GitHub and Initial Deployment
* [x] Sprint 6 - Dockerize and Deploy Backend on Railway
* [x] Sprint 7 - Deploy Frontend on Vercel and Configure CORS
* [x] Sprint 8 - Harden Backend Configuration and Health Checks
* [x] Sprint 9 - Add Pydantic Response Models and Improve API Documentation

---

## 🔮 Future Improvements

* Add filtering by infrastructure type
* Improve GeoJSON schema typing
* Add authentication / API keys
* Implement performance optimizations (vector tiles)
* Add monitoring and logging improvements

---

## 👤 Author

GitHub: https://github.com/Alpha199777
