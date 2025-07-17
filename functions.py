import os
import subprocess
import threading

def run_in_thread(func):
    def wrapper(*args, **kwargs):
        threading.Thread(target=func, args=args, kwargs=kwargs, daemon=True).start()
    return wrapper

@run_in_thread
def nvidia_smi(show_output):
    cmd = "nvidia-smi"
    try:
        result = subprocess.check_output(cmd.split(), text=True, timeout=10)
    except Exception as e:
        result = f"Error: {e}"
    show_output(f"{cmd}\n\n{result}")

@run_in_thread
def driver_info(show_output):
    cmd = "modinfo -F version nvidia"
    try:
        result = subprocess.check_output(cmd.split(), text=True)
        result = f"Nvidia Driver Version: {result.strip()}"
    except Exception as e:
        result = f"Error: {e}"
    show_output(f"{cmd}\n\n{result}")

@run_in_thread
def gpu_usage(show_output):
    cmd = "nvidia-smi --query-gpu=utilization.gpu,memory.used,memory.total --format=csv"
    try:
        result = subprocess.check_output(cmd.split(), text=True)
    except Exception as e:
        result = f"Error: {e}"
    show_output(f"{cmd}\n\n{result}")

@run_in_thread
def xorg_log(show_output):
    cmd = "tail -n 40 /var/log/Xorg.0.log"
    try:
        result = subprocess.check_output(cmd.split(), text=True)
    except Exception as e:
        result = f"Error: {e}"
    show_output(f"{cmd}\n\n{result}")

def btrfs_send(show_output):
    cmd = "btrfs send"
    show_output(f"{cmd}\n\n(hier könnte ein Befehl stehen)")

@run_in_thread
def btrfs_list(show_output):
    cmd = "btrfs filesystem show"
    try:
        result = subprocess.check_output(cmd.split(), text=True)
    except Exception as e:
        result = f"Error: {e}"
    show_output(f"{cmd}\n\n{result}")

@run_in_thread
def systemd_list(show_output):
    cmd = "systemctl list-units --type=service --state=running"
    try:
        result = subprocess.check_output(cmd.split(), text=True)
    except Exception as e:
        result = f"Error: {e}"
    show_output(f"{cmd}\n\n{result}")

@run_in_thread
def systemd_failed(show_output):
    cmd = "systemctl --failed"
    try:
        result = subprocess.check_output(cmd.split(), text=True)
    except Exception as e:
        result = f"Error: {e}"
    show_output(f"{cmd}\n\n{result}")

@run_in_thread
def systemd_analyze(show_output):
    cmd = "systemd-analyze"
    try:
        result = subprocess.check_output(cmd.split(), text=True)
    except Exception as e:
        result = f"Error: {e}"
    show_output(f"{cmd}\n\n{result}")

@run_in_thread
def kernel_version(show_output):
    cmd = "uname -r"
    try:
        result = subprocess.check_output(cmd.split(), text=True)
        result = f"Current Kernel: {result.strip()}"
    except Exception as e:
        result = f"Error: {e}"
    show_output(f"{cmd}\n\n{result}")

@run_in_thread
def list_kernels(show_output):
    cmd = "ls /boot"
    try:
        result = subprocess.check_output(cmd.split(), text=True)
    except Exception as e:
        result = f"Error: {e}"
    show_output(f"{cmd}\n\n{result}")

@run_in_thread
def check_updates(show_output):
    cmd = "checkupdates"
    try:
        result = subprocess.check_output(cmd.split(), text=True)
    except Exception as e:
        result = f"Error: {e}\n(Tipp: checkupdates ist auf Arch, für Debian/Ubuntu: apt list --upgradable)"
    show_output(f"{cmd}\n\n{result}")

@run_in_thread
def list_orphans(show_output):
    cmd = "pacman -Qdt"
    try:
        result = subprocess.check_output(cmd.split(), text=True)
    except Exception as e:
        result = f"Error: {e}"
    show_output(f"{cmd}\n\n{result}")

@run_in_thread
def wifi_list(show_output):
    cmd = "nmcli device wifi list"
    try:
        result = subprocess.check_output(cmd.split(), text=True)
    except Exception as e:
        result = f"Error: {e}"
    show_output(f"{cmd}\n\n{result}")

@run_in_thread
def wifi_current(show_output):
    cmd = "nmcli -t -f active,ssid dev wifi"
    try:
        result = subprocess.check_output(cmd.split(), text=True)
    except Exception as e:
        result = f"Error: {e}"
    show_output(f"{cmd}\n\n{result}")

@run_in_thread
def ssh_config(show_output):
    cmd = "cat ~/.ssh/config"
    path = os.path.expanduser("~/.ssh/config")
    try:
        if not os.path.exists(path):
            result = "Datei existiert nicht."
        else:
            with open(path, "r") as f:
                result = f.read()
    except Exception as e:
        result = f"Error: {e}"
    show_output(f"{cmd}\n\n{result}")

@run_in_thread
def ssh_known_hosts(show_output):
    cmd = "cat ~/.ssh/known_hosts"
    path = os.path.expanduser("~/.ssh/known_hosts")
    try:
        if not os.path.exists(path):
            result = "Datei existiert nicht."
        else:
            with open(path, "r") as f:
                result = f.read()
    except Exception as e:
        result = f"Error: {e}"
    show_output(f"{cmd}\n\n{result}")

@run_in_thread
def cpu_info(show_output):
    cmd = "lscpu"
    try:
        result = subprocess.check_output(cmd.split(), text=True)
    except Exception as e:
        result = f"Error: {e}"
    show_output(f"{cmd}\n\n{result}")

@run_in_thread
def cpu_usage(show_output):
    cmd = "top -b -n 1"
    try:
        result = subprocess.check_output(cmd.split(), text=True)
        result = "\n".join(result.splitlines()[:20])
    except Exception as e:
        result = f"Error: {e}"
    show_output(f"{cmd}\n\n{result}")

@run_in_thread
def list_disks(show_output):
    cmd = "lsblk -o NAME,SIZE,TYPE,MOUNTPOINT"
    try:
        result = subprocess.check_output(cmd.split(), text=True)
    except Exception as e:
        result = f"Error: {e}"
    show_output(f"{cmd}\n\n{result}")

@run_in_thread
def smart_status(show_output):
    cmd = "smartctl -H /dev/sda"
    try:
        result = subprocess.check_output(cmd.split(), text=True)
    except Exception as e:
        result = f"Error: {e}\n(Tipp: smartmontools muss installiert sein und /dev/sda existieren)"
    show_output(f"{cmd}\n\n{result}")

@run_in_thread
def list_mounts(show_output):
    cmd = "cat /etc/fstab"
    try:
        result = subprocess.check_output(cmd.split(), text=True)
    except Exception as e:
        result = f"Error: {e}"
    show_output(f"{cmd}\n\n{result}")

@run_in_thread
def pacman_log(show_output):
    cmd = "tail -n 40 /var/log/pacman.log"
    try:
        result = subprocess.check_output(cmd.split(), text=True)
    except Exception as e:
        result = f"Error: {e}"
    show_output(f"{cmd}\n\n{result}")

@run_in_thread
def pacman_foreign(show_output):
    cmd = "pacman -Qm"
    try:
        result = subprocess.check_output(cmd.split(), text=True)
    except Exception as e:
        result = f"Error: {e}"
    show_output(f"{cmd}\n\n{result}")

@run_in_thread
def journalctl(show_output):
    cmd = "journalctl -n 40"
    try:
        result = subprocess.check_output(cmd.split(), text=True)
    except Exception as e:
        result = f"Error: {e}"
    show_output(f"{cmd}\n\n{result}")

@run_in_thread
def dmesg(show_output):
    cmd = "dmesg -T --level=err,warn"
    try:
        result = subprocess.check_output(cmd.split(), text=True)
    except Exception as e:
        result = f"Error: {e}"
    show_output(f"{cmd}\n\n{result}")

@run_in_thread
def fastfetch(show_output):
    cmd = "fastfetch"
    try:
        result = subprocess.check_output(cmd.split(), text=True)
    except Exception as e:
        result = f"Error: {e}"
    show_output(f"{cmd}\n\n{result}")

@run_in_thread
def lsb_release(show_output):
    cmd = "lsb_release -a"
    try:
        result = subprocess.check_output(cmd.split(), text=True)
    except Exception as e:
        result = f"Error: {e}"
    show_output(f"{cmd}\n\n{result}")

# Zusätzliche harmlose Info-Befehle:

@run_in_thread
def hostnamectl(show_output):
    cmd = "hostnamectl"
    try:
        result = subprocess.check_output(cmd.split(), text=True)
    except Exception as e:
        result = f"Error: {e}"
    show_output(f"{cmd}\n\n{result}")

@run_in_thread
def free(show_output):
    cmd = "free -h"
    try:
        result = subprocess.check_output(cmd.split(), text=True)
    except Exception as e:
        result = f"Error: {e}"
    show_output(f"{cmd}\n\n{result}")

@run_in_thread
def uptime(show_output):
    cmd = "uptime"
    try:
        result = subprocess.check_output(cmd.split(), text=True)
    except Exception as e:
        result = f"Error: {e}"
    show_output(f"{cmd}\n\n{result}")