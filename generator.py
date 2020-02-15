import uuid
import csv
import os
from faker import Faker

fake = Faker()

for file_index in range(100):
    file_name = str(uuid.uuid4()) + ".csv"
    file_path = "./data/" + file_name
    with open(file_path, 'w') as file:
        writer = csv.DictWriter(file, fieldnames=["name", "country"])
        writer.writeheader()
        for person_index in range(10000):    
            writer.writerow({'name': fake.name(), 'country': fake.country()})