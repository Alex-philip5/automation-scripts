import time
import psutil
import os
from datetime import datetime

def get_high_cpu_processes(threshold=10.0, duration=10):
    high_cpu_processes = []

    for _ in range(duration):
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
            if proc.info['cpu_percent'] > threshold:
                if proc.info['pid'] not in [p['pid'] for p in high_cpu_processes]:
                    high_cpu_processes.append(proc.info)
        time.sleep(1)

    return high_cpu_processes

def kill_high_cpu_processes(high_cpu_processes):
    for proc in high_cpu_processes:
        try:
            p = psutil.Process(proc['pid'])
            p.terminate()
        except psutil.NoSuchProcess:
            print(f"Process with PID {proc['pid']} does not exist.")

def main():
    high_cpu_processes = get_high_cpu_processes()
    with open(f"high_cpu_processes_{datetime.now().strftime('%Y_%m_%d')}.log", 'w') as f:
        for proc in high_cpu_processes:
            f.write(f"PID: {proc['pid']}, Process Name: {proc['name']}, CPU Utilization: {proc['cpu_percent']}%\n")
    kill_high_cpu_processes(high_cpu_processes)

if __name__ == "__main__":
    main()

