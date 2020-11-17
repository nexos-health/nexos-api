# Start from python image
FROM python:3.7.8

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH .
ENV PEEPS_HOST https://nexoshealth.com.au:8000
ENV PORT 5000

# Create src directory
RUN mkdir /src
WORKDIR /src

# Install requirements
COPY requirements.txt /src/
RUN pip install -r requirements.txt

# Copy files to image
COPY src /src/

# Commands to run on startup of container
CMD exec gunicorn --bind :$PORT --workers 3 --timeout 0 wsgi:app
#CMD ["gunicorn", "--workers", "3", "--bind", "0.0.0.0:5000", "wsgi:app"]
