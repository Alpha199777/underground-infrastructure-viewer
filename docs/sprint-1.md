# Sprint 1 — Architecture & Project Setup

## Goal
Establish a clean, professional project foundation that mirrors real-world GIS engineering workflows.

## Structure Created
\\\
underground-infrastructure-viewer/
+-- backend/        # FastAPI application, database logic, API routes
+-- frontend/       # Map client application
+-- docs/           # Sprint documentation and architecture notes
+-- data/           # GeoJSON and geospatial source files
+-- .gitignore      # Version control exclusion rules
+-- docs/sprint-1.md
\\\

## Decisions Made
- Monorepo structure: frontend and backend in one repository
- Clean separation of concerns enforced from Day 1
- Git initialized before any code — full history tracked
- .gitignore configured to protect secrets and exclude large GIS files

## Tech Stack Confirmed
- Frontend: MapLibre GL JS
- Backend: Python / FastAPI
- Database: PostgreSQL + PostGIS
- Format: GeoJSON
- Version Control: Git
