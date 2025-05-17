#!/usr/bin/env python3
"""
Block URLs by rerouting them to localhost through
the addition of rules in the system's hosts file.
"""

import platform
import re


def get_os_name():
    """Get the current OS name."""
    return platform.system()


def get_hosts_path():
    """Determine the path to the hosts based on the current OS."""
    system_name = get_os_name()
    if system_name == "Windows":
        return "C:\\Windows\\System32\\drivers\\etc\\hosts"
    if system_name == "Linux":
        return "/etc/hosts"
    raise OSError("Unsupported OS!")


def prompt_for_number_of_pages():
    """Prompt for an integer"""
    while True:
        try:
            return int(input("Number of pages: "))
        except ValueError:
            print("Incorrect input. Enter an integer!")


def prompt_for_url():
    """Prompt for a link and ensure it doesn't contain unnecessary prefix"""
    url = input("Enter URL: ").strip()
    return re.sub(r"^(?:https?://)?(?:www\.)?", "", url)


def get_all_possible_urls(urls):
    """Generate a list of URLs with common prefixes: 'www', 'http', 'https'"""
    urls = urls + [("www." + url) for url in urls]
    return (
        urls
        + [("http://" + url) for url in urls]
        + [("https://" + url) for url in urls]
    )


def ipv4_block_entry(url):
    """Generate an IPv4 block entry for a given URL."""
    return "0.0.0.0" + "\t\t" + url + "\n"


def ipv6_block_entry(url):
    """Generate an IPv6 block entry for a given URL."""
    return "::1" + "\t\t" + url + "\n"


def append_to_hosts(urls, hosts_path):
    """Append URLs to the hosts file to block them."""
    with open(hosts_path, "a", encoding="utf-8") as hosts_file:
        hosts_file.write("\n")
        for url in urls:
            hosts_file.write(ipv4_block_entry(url))
            hosts_file.write(ipv6_block_entry(url))
    print("URLs have been successfully blocked!")


def check_is_sudo(system_name):
    if system_name == "Linux":
        import os

        return os.geteuid() == 0

    if system_name == "Windows":
        import ctypes

        return ctypes.windll.shell32.IsUserAnAdmin() != 0


def main():
    """Prompt for urls and append them to the hosts file to block them"""

    system_name = get_os_name()
    if not check_is_sudo(system_name):
        exit("User does NOT HAVE SUDO")

    hosts_path = get_hosts_path()
    n = prompt_for_number_of_pages()
    urls = []
    for _ in range(n):
        urls.append(prompt_for_url())
    append_to_hosts(get_all_possible_urls(urls), hosts_path)


if __name__ == "__main__":
    main()
