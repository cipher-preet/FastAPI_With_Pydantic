# use Python 3.11 base image
FROM python:3.11-slim

# set working Directory
WORKDIR /app

# copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#copy rest of application code (app.py,model.py,frontend.py etc)
COPY . .

# expose rthe application port
EXPOSE 8000

# commandf to start FAST API application
CMD ["uvicorn","app:app", "--host","0.0.0.0","--port","8000"]
