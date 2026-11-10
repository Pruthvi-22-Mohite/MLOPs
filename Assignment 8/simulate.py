import requests
import random
import time
import sys

URL = "http://localhost:8000"

mode = sys.argv[1] if len(sys.argv) > 1 else "normal"

def generate_sample():
    return {
        "sepal_length": random.uniform(4.5, 7.5),
        "sepal_width": random.uniform(2.0, 4.5),
        "petal_length": random.uniform(1.0, 6.5),
        "petal_width": random.uniform(0.1, 2.5)
    }

print("Starting traffic simulation:", mode)

for i in range(100):

    if mode == "errors" and random.random() < 0.3:
        response = requests.post(
            f"{URL}/predict",
            json={"invalid": "data"}
        )
    else:
        response = requests.post(
            f"{URL}/predict",
            json=generate_sample()
        )

    print(f"Request {i+1}: Status Code = {response.status_code}")

    time.sleep(0.2)

print("Traffic simulation completed!")