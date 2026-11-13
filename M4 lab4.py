import json

# Create sample JSON log file
sample_logs = [
    {"time": "10:00", "level": "INFO", "message": "Server started"},
    {"time": "10:05", "level": "ERROR", "message": "Database failed"},
    {"time": "10:10", "level": "WARNING", "message": "High CPU usage"},
    {"time": "10:15", "level": "ERROR", "message": "Login timeout"},
    {"time": "10:20", "level": "INFO", "message": "Backup completed"}
]

file = open("logs.json", "w")
json.dump(sample_logs, file, indent=4)
file.close()

# Read and analyze JSON logs
file = open("logs.json", "r")
logs = json.load(file)
file.close()

info_count = 0
warning_count = 0
error_count = 0

for entry in logs:
    if entry["level"] == "INFO":
        info_count = info_count + 1
    elif entry["level"] == "WARNING":
        warning_count = warning_count + 1
    elif entry["level"] == "ERROR":
        error_count = error_count + 1

print("--- JSON LOG ANALYSIS ---")
print("Total Logs:", len(logs))
print("INFO:", info_count)
print("WARNING:", warning_count)
print("ERROR:", error_count)

print("\n--- ERROR DETAILS ---")
for entry in logs:
    if entry["level"] == "ERROR":
        print("Time:", entry["time"], "| Message:", entry["message"])