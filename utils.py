import psutil
import datetime

def get_system_metrics():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"[{timestamp}] CPU: {cpu}% | RAM: {ram}% | Disk: {disk}%"

def log_metrics(data):
    with open("log.txt", "a") as f:
        f.write(data + "\n")

def check_alert(data):
    cpu_usage = float(data.split("CPU: ")[1].split("%")[0])
    if cpu_usage > 80:
        print("[ALERT] High CPU usage detected!")

