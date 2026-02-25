import os
import subprocess
import time

def log_event(msg):
    print(f"[SENTINEL] {msg}")
    # 后续可以集成 message.send 发送给 Telegram

def check_docker():
    try:
        status = subprocess.check_output("docker inspect -f '{{.State.Running}}' antigravity-manager", shell=True).decode().strip()
        if status != 'true':
            log_event("Detecting antigravity-manager DOWN. Restarting...")
            os.system("docker restart antigravity-manager")
    except Exception as e:
        log_event(f"Docker check error: {e}")

def check_disk():
    # 清理缓存逻辑
    cache_path = "/root/.cache/pip"
    if os.path.exists(cache_path):
        size_gb = int(subprocess.check_output(f"du -s {cache_path} | cut -f1", shell=True)) / 1024 / 1024
        if size_gb > 3:
            log_event(f"Pip cache too large ({size_gb:.2f}GB). Cleaning...")
            os.system(f"rm -rf {cache_path}/*")

if __name__ == "__main__":
    log_event("Sentinel Service Started.")
    check_docker()
    check_disk()
