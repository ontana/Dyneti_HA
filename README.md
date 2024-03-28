# Dyneti_HA

## Overview
This project is using simple Tensorflow model and Flask to receive request from Restful API and give result whether object in image is dog or cat
Database to store prediction value is SQLite.

Project is built using Python3.11 and above

## How to run
1. Setup Python virtual environment
```bash
python3 -m venv ./venv
source venv/bin/activate
```
2. Install requirement package:
```bash
pip3 install -r requirements.txt
```
3. Config threshold value for prediction: `flask_api/config/config.json`
```bash
"model_idx": 0 // model will return 2 or more prediction score. Each score will be for 1 kind of animal
"threshold": 0.8 // Threshold value to detect of object is matched
```
4. Start Restful API:
```bash
python3 flask_api/server.py
```