#! python3
"""
This simple Python script allows you to easily block URLs by rerouting them to localhost
through the addition of rules in the system's hosts file.
"""

import os
import sys


def all_possible_urls(urls):
    """
    :param urls:
    :return:
    """
    www_urls = [('www.' + url) for url in urls]
    http_urls = [('http://' + url) for url in urls]
    https_urls = [('https://' + url) for url in urls]
    http_www_urls = [('http://' + url) for url in www_urls]
    https_www_urls = [('https://' + url) for url in www_urls]
    all_urls = urls + www_urls + http_urls + https_urls + http_www_urls + https_www_urls
    return all_urls


def main():
    hosts_path = 'C:\\Windows\\System32\\drivers\\etc\\hosts'

    try:
        if not os.path.exists(hosts_path):
            raise FileNotFoundError
    except FileNotFoundError:
        print(f"{hosts_path} doesn't exist!")
        sys.exit(1)

    urls = []
    n = int(input("Number of pages to block: "))
    for _ in range(n):
        urls.append(input("url: "))

    with open(hosts_path, 'a', encoding='utf-8') as hosts_file:
        for url in all_possible_urls(urls):
            hosts_file.write('127.0.0.1' + '\t\t' + url + '\n')


if __name__ == '__main__':
    main()
