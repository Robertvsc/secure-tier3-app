# Secure 3-Tier Web Architecture with CI/CD & Disaster Recovery

## 📋 Overview
A production-ready, containerized web application stack built with **Docker Compose**. This project demonstrates the following practices - **Security Hardening**, **Automated Backups**, and a full **CI/CD Pipeline**.

The architecture consists of a Python Flask backend, a PostgreSQL database, and a sidecar backup service, all orchestrated to ensure high availability and data persistence.

## 🏗 Architecture
- **App Service:** Python Flask API running as a **non-root user** for security.
- **Database:** PostgreSQL 13 with persistent volume storage.
- **Backup Sidecar:** A dedicated container performing automated logical backups (`pg_dump`) every minute.
- **Orchestration:** Docker Compose with **Healthchecks** to ensure zero-downtime startup dependency management.

## 🚀 Key Features
- **Security First:**
  - Non-root user execution in Dockerfiles.
  - Secrets management via `.env` files (no hardcoded credentials).
  - Vulnerability scanning via **Trivy** in CI/CD.
- **Resilience:**
  - `healthcheck` implementation prevents the app from starting before the DB is ready.
  - Automatic restart policies.
- **CI/CD Pipeline:**
  - GitHub Actions workflow that automatically builds, scans, and pushes images to Docker Hub on every commit.

## 🛠 Tech Stack
- **Containerization:** Docker & Docker Compose
- **Backend:** Python (Flask), Psycopg2
- **Database:** PostgreSQL
- **Automation:** Bash Scripting (Backup), GitHub Actions (CI/CD)
- **Security:** Trivy (Image Scanning)
