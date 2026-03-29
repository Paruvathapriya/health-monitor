import random
import time
import json

records = []

# 10 patients
patients = [f"P{i}" for i in range(1, 11)]

while True:
    for patient_id in patients:

        # Decide NORMAL or ALERT (70% NORMAL)
        if random.random() < 0.7:
            # NORMAL values
            heart_rate = random.randint(65, 95)
            oxygen = random.randint(95, 100)
            temperature = round(random.uniform(36.0, 37.5), 1)
            systolic = random.randint(110, 130)
            diastolic = random.randint(70, 85)
            status = "NORMAL"

        else:
            # ALERT values
            heart_rate = random.choice([
                random.randint(40, 55),
                random.randint(105, 130)
            ])
            oxygen = random.randint(80, 91)
            temperature = round(random.uniform(38.0, 40.0), 1)
            systolic = random.randint(140, 170)
            diastolic = random.randint(90, 110)
            status = "ALERT"

        blood_pressure = f"{systolic}/{diastolic}"

        # Store record
        records.append({
            "patient_id": patient_id,
            "heart_rate": heart_rate,
            "oxygen_level": oxygen,
            "temperature": temperature,
            "blood_pressure": blood_pressure,
            "status": status
        })

        # Full print (fixed)
        print(f"Inserted → {patient_id}, HR:{heart_rate}, O2:{oxygen}, Temp:{temperature}, BP:{blood_pressure}, Status:{status}")

        time.sleep(1)

    # Save JSON after each full cycle (all 10 patients)
    with open('../app/data.json', 'w') as f:
        json.dump(records[-100:], f, indent=4)

    print("✅ JSON updated!", flush=True)
