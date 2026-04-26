# 🌍 Climate Challenge - Week 0

## 📌 Project Overview
This project is part of the Climate Challenge Week 0 assignment.  
It demonstrates how to set up a clean Python development environment, organize a project properly, and use GitHub Actions for Continuous Integration (CI).

---

## 🚀 How to Reproduce the Environment

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/climate-challenge-week0.git
cd climate-challenge-week0
## How to Run the Project

### 1. Clone repo
git clone <repo-url>
cd climate-challenge-week0

### 2. Create virtual environment
python -m venv .venv

### 3. Activate environment
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate      # Windows

### 4. Install dependencies
pip install -r requirements.txt

## Project Structure
climate-challenge-week0/
│── .github/
│   └── workflows/
│       └── unittests.yml
│── notebooks/
│   ├── README.md
│── scripts/
│   ├── __init__.py
│   └── README.md
│── src/
│   ├── __init__.py
│── tests/
│   ├── __init__.py
│── .gitignore
│── requirements.txt
│── README.md
│── .venv/ (excluded from GitHub)
✅ CI

GitHub Actions is configured to automatically install dependencies on push.