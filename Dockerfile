#base image
FROM python:3.9-slim

#working directory
WORKDIR /app
#copy requirements file
COPY . /app 
 #run
 RUN pip install --no-cache-dir -r requirements.txt

 #port
    EXPOSE 8000

    #command
    CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]