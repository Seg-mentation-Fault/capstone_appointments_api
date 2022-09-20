# MEDAPP API
 
![image](https://user-images.githubusercontent.com/77710222/191312115-79206a3e-09c5-4bef-b956-212cbb7a6434.png)


See the documentation [here](https://capstone-appointments-api-ta75cu5v6q-ue.a.run.app/docs)


source venv/bin/activate
cd app/

- uvicorn main:app --reload
- gunicorn --bind :$PORT --workers 1 --worker-class uvicorn.workers.UvicornWorker --threads 8 app.main:app
