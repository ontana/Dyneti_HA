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
"threshold": 0.8 // Threshold value to detect of object is matched. Adjust it to reasonable value
```
4. Start Restful API:
```bash
python3 flask_api/server.py
```
Wait until there is line `* Running on http://127.0.0.1:5000`
5. Run testing script: Add images to `scripts/sample`
```bash
cd scripts/
python3 sample_script.py
```
6. Using webcam capture script:
```bash
cd scripts/
python3 webcam_capture.py
```
```warn
First run will always be failed due to permission for terminal to access Webcam.
Click Allow to access and re-run will give correct result
```
7. Install SQLite driver and check database in `instance/dyneti.db`