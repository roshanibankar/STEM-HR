# STEMHR Project

## Overview
This is a private Django-based HR management application developed exclusively for [Company Name]. This project is not intended for public use or distribution.

## Important Notice
⚠️ **This repository contains proprietary code and is confidential. Unauthorized use, copying or sharing is strictly prohibited.**

## Internal Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <internal-repo-url>
   cd STEMHR

## Internal Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <internal-repo-url>
   cd STEMHR

2. **Create and activate a virtual environment**
```bash
# On macOS/Linux:
python -m venv env
source env/bin/activate

# On Windows:
python -m venv env
env\Scripts\activate
```
3. **Install dependencies**
```bash
pip install -r requirements.txt
```
4. **Apply database migrations**
```bash
python manage.py migrate
```
5. **Run the developement server**
```bash
python manage.py runserver
```
6. **Access the app**
Open your browser and go to:
```bash 
# http://127.0.0.1:8000/
```
