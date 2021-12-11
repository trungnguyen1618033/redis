# redis
Basic redis + fastAPI

Setup:
- python3 -m venv .venv
- source .venv/bin/activate
- pip install fastapi[all]
- pip3 install redis
- sudo apt install redis-server

Run: 
 uvicorn main:app --host 0.0.0.0 --port 8000
