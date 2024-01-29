import time
import psutil
from datetime import datetime

def get_high_cpu_processes(threshold=65.0, duration=10):
    high_cpu_processes = []

    for _ in range(duration):
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'username', 'cmdline']):
            if proc.info['cpu_percent'] > threshold:
                if proc.info['pid'] not in [p['pid'] for p in high_cpu_processes]:
                    high_cpu_processes.append(proc.info)
        time.sleep(1)

    return high_cpu_processes


# def log_high_cpu_processes(high_cpu_processes):
#     with open(f"high_cpu_processes_{datetime.now().strftime('%Y_%m_%d')}.log", 'w') as f:
#         for proc in high_cpu_processes:
#             f.write(f"Timestamp: {datetime.now()}, PID: {proc['pid']}, Process Name: {proc['name']}, CPU Utilization: {proc['cpu_percent']}%, User: {proc['username']}, Command: {' '.join(proc['cmdline'])}\n")

def log_high_cpu_processes(high_cpu_processes):
    with open(f"high_cpu_processes_{datetime.now().strftime('%Y_%m_%d')}.log", 'a') as f:  # Open file in append mode
        for proc in high_cpu_processes:
            f.write(f"Timestamp: {datetime.now()}, PID: {proc['pid']}, Process Name: {proc['name']}, CPU Utilization: {proc['cpu_percent']}%, User: {proc['username']}, Command: {' '.join(proc['cmdline'])}\n")


def main():
    high_cpu_processes = get_high_cpu_processes()
    log_high_cpu_processes(high_cpu_processes)

if __name__ == "__main__":
    main()
