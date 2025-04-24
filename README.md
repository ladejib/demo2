# demo2

### Run normally:
pytest

### Run with 4 parallel workers:
pytest -n 4 --env=qa

### Generate Allure Report:
allure serve reports/allure

# Build Docker image
docker build --no-cache -t flask-api .

# Run the container
docker run -d -p 5000:5000 --name flask-api flask-api

/Users/saifbiobaku/project4/myvenv/bin/pytest tests/ --html=report.html

docker-compose up --build --abort-on-container-exit

