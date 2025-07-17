# variables.py

TOPICS = {
    "Display": ["Nvidia", "Xorg", "Wayland"],
    "System": ["Btrfs", "Grep", "Systemd", "Kernel", "Updates", "Services"],
    "Network": ["Rclone", "WiFi", "Ethernet", "Firewall", "SSH"],
    "Hardware": ["CPU", "RAM", "Disks", "USB", "Sensors"],
    "Package": ["Pacman", "AUR", "Flatpak", "Snap"],
    "User": ["Accounts", "Groups", "Permissions"],
    "Security": ["Firewall", "Fail2Ban", "AppArmor", "SELinux"],
    "Maintenance": ["Logs", "Cleanup", "Backups", "Crontab"],
    "Info": ["System Info", "Distro", "Uptime", "Resources"],
}

FUNCTIONS = {
    ("Display", "Nvidia"): [
        {"label": "nvidia-smi", "function": "nvidia_smi"},
        {"label": "Driver Info", "function": "driver_info"},
        {"label": "GPU Usage", "function": "gpu_usage"},
        {"label": "Xorg Log", "function": "xorg_log"},
    ],
        ("System", "Btrfs"): [
        {"label": "List Btrfs", "function": "btrfs_list"},
    ],
    ("System", "Systemd"): [
        {"label": "List Services", "function": "systemd_list"},
        {"label": "Failed Services", "function": "systemd_failed"},
        {"label": "Analyze Boot", "function": "systemd_analyze"},
    ],
    ("System", "Kernel"): [
        {"label": "Current Kernel", "function": "kernel_version"},
        {"label": "List Kernels", "function": "list_kernels"},
    ],
    ("System", "Updates"): [
        {"label": "Check Updates", "function": "check_updates"},
        {"label": "List Orphans", "function": "list_orphans"},
    ],
    ("Network", "WiFi"): [
        {"label": "List Networks", "function": "wifi_list"},
        {"label": "Current Connection", "function": "wifi_current"},
    ],
    ("Network", "SSH"): [
        {"label": "SSH Config", "function": "ssh_config"},
        {"label": "Known Hosts", "function": "ssh_known_hosts"},
    ],
    ("Hardware", "CPU"): [
        {"label": "CPU Info", "function": "cpu_info"},
        {"label": "CPU Usage", "function": "cpu_usage"},
    ],
    ("Hardware", "Disks"): [
        {"label": "List Disks", "function": "list_disks"},
        {"label": "SMART Status", "function": "smart_status"},
        {"label": "Mounts/fstab", "function": "list_mounts"},

    ],
    ("Package", "Pacman"): [
        {"label": "Pacman Log", "function": "pacman_log"},
        {"label": "List Foreign", "function": "pacman_foreign"},
    ],
    ("Maintenance", "Logs"): [
        {"label": "Journalctl", "function": "journalctl"},
        {"label": "dmesg", "function": "dmesg"},
    ],
    ("Info", "System Info"): [
        {"label": "fastfetch", "function": "fastfetch"},
        {"label": "lsb_release", "function": "lsb_release"},
    ],
    # ... und so weiter!
}