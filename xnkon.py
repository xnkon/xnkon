#!/usr/bin/env python
"""
Print a random Zen Koan to the screen

A random Zen Koan is requested from cincinato.org/koans
Credit to James Collado for maintaining the english and spanish database of Zen Koans and having it open to the public (more info: http://cincinato.org/koans/about_en.php)

Please add the following to your .bashrc, .bash_profile, etc to make available in your shell:
```
export PATH=$PATH:/path/to/xnkon
```
"""
from argparse import ArgumentParser
import requests


def koan():
    URL = "https://cincinato.org/koans/randomkoan_en.php"
    headers = {
        "Host": "cincinato.org",
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:127.0) Gecko/20100101 Firefox/127.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Priority": "u=1"
    }

    try:
        resp = requests.get(URL, headers=headers)

        text = resp.text.split('<h2>')[1]

        italic_title = f"\033[3m{text.split('</h2>')[0].replace('\n', '')}\033[0m" 
        print(italic_title)
        for p in text.split('/center>\n')[1].split('<center>')[0].split('<p>')[2:-1]:
            t = ' '.join(
                l for l in
                    p.replace('</p>', '')
                        .replace('&nbsp; ', '')
                        .replace('&nbsp;', '')
                        .split('\n')
                if l != '' and not l.isspace()
            ).replace('  ', ' ')
            print(f"> {t}")
                                                     

    except:
        pass


if __name__ == '__main__':
    parser = ArgumentParser(description="Retrieve a random Zen Koan from an online database")

    koan()

