#! python3
"""
This simple Python script allows you to easily block URLs by rerouting them to localhost
through the addition of rules in the system's hosts file.
"""

import os
import platform
import sys


def determine_host_path():
    """
    Determine the path to the hosts based on the current OS.

    :return:
        str: The file path to the hosts file.
    """
    system_name = platform.system()
    if system_name == 'Windows':
        return 'C:\\Windows\\System32\\drivers\\etc\\hosts'
    if system_name == 'Linux':
        return '/etc/hosts'
    raise OSError('Unsupported OS!')


def all_possible_urls(urls):
    """
    Generate a list of URLs including variations prefixed with 'www', 'http', and 'https'.

    :param urls: a list of urls to expand
    :return:
        list of str: list including original urls and prefixed urls
    """
    www_urls = [('www.' + url) for url in urls]
    http_urls = [('http://' + url) for url in urls]
    https_urls = [('https://' + url) for url in urls]
    http_www_urls = [('http://' + url) for url in www_urls]
    https_www_urls = [('https://' + url) for url in www_urls]
    all_urls = urls + www_urls + http_urls + https_urls + http_www_urls + https_www_urls
    return all_urls


def main():
    try:
        hosts_path = determine_host_path()
        if not os.path.exists(hosts_path):
            raise FileNotFoundError(f"{hosts_path} doesn't exist!")

        urls = []
        while True:
            try:
                n = int(input("Number of pages to block: "))
            except ValueError:
                print("Number of pages must be an integer!")
            else:
                break
        
        for _ in range(n):
            urls.append(input("url: "))

        with open(hosts_path, 'a', encoding='utf-8') as hosts_file:
            hosts_file.write('\n')
            for url in all_possible_urls(urls):
                hosts_file.write('0.0.0.0' + '\t\t' + url + '\n')
        print("URLs has been successfully blocked!")

    except (OSError, FileNotFoundError) as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
