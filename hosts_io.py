# .!/usr/bin/env python3
"""
Export current hosts settings to path provided or Desktop
"""
import os
import shutil

from main import get_hosts_path


def get_desktop_path():
    return os.path.join(os.path.expanduser("~"), "Desktop")


def export_hosts_file(path=get_desktop_path()):
    hosts_path = get_hosts_path()
    try:
        shutil.copy2(hosts_path, path)
    except FileNotFoundError as e:
        print(f"Error while exporting! {e}")


def import_hosts_file(path=os.path.join(get_desktop_path(), "hosts.txt")):
    try:
        shutil.copy2(path, get_hosts_path())
    except Exception as e:
        print(f"Error while importing! {e}")


def list_blocked_pages():
    urls = []
    with open(get_hosts_path()) as file:
        for line in file:
            if line.strip():
                if not line.strip().startswith("#"):
                    ip, url, *comment = line.split()
                    if ip in ["0.0.0.0", "127.0.0.1"]:
                        urls.append(url)
    return urls


def list_unique_blocked_pages():
    return list(set(list_blocked_pages()))


def export_blocked_pages(path=get_desktop_path()):
    blocked_pages = list_unique_blocked_pages()
    with open(os.path.join(path, "blocked_pages.txt"), "w") as file:
        for page in blocked_pages:
            file.write(f"{page} \n")
