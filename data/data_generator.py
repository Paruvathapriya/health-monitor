import random
import time
import json

print("✅ Script started", flush=True)

records = []

for i in range(100):
    print(f"Loop {i+1}", flush=True)

    patient_id = random.choice(["P1", "P2", "P3"])

    # 👉 70% NORMAL, 30% ALERT
    if random.random() < 0.7:
        # NORMAL DATA
        heart_rate = random.randint(65, 95)
        oxygen = random.randint(94, 100)
        temperature = round(random.uniform(36.2, 37.5), 1)
        systolic = random.randint(110, 130)
        diastolic = random.randint(70, 85)
    else:
        # ABNORMAL DATA
        heart_rate = random.choice([
            random.randint(40, 55),   # low
            random.randint(105, 130)  # high
        ])
        oxygen = random.randint(80, 91)
        temperature = round(random.uniform(38.0, 40.0), 1)
        systolic = random.randint(140, 170)
        diastolic = random.randint(90, 110)

    blood_pressure = f"{systolic}/{diastolic}"

    # Status logic
    status = "NORMAL"
    if (heart_rate > 100 or heart_rate < 60 or
        oxygen < 92 or
        temperature > 38 or
        systolic > 140 or diastolic > 90):
        status = "ALERT"

    # Store record
    records.append({
        "patient_id": patient_id,
        "heart_rate": heart_rate,
        "oxygen_level": oxygen,
        "temperature": temperature,
        "blood_pressure": blood_pressure,
        "status": status
    })

    # Full print (ALL values)
    print(f"Inserted → {patient_id}, HR:{heart_rate}, O2:{oxygen}, Temp:{temperature}, BP:{blood_pressure}, Status:{status}", flush=True)

    time.sleep(1)

# Save JSON
with open('../app/data.json', 'w') as f:
    json.dump(records, f, indent=4)

print("✅ JSON created successfully!", flush=True)
