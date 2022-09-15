# Capstone Appointments API

source venv/bin/activate
cd app/

- uvicorn main:app --reload
- gunicorn --bind :$PORT --workers 1 --worker-class uvicorn.workers.UvicornWorker --threads 8 app.main:app
