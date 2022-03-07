#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import time


def main():

    with open("imagelist.txt", "w") as fobj:
        for issue in range(142, 200):
            time.sleep(1)
            html = requests.get(
                f"https://marvel.fandom.com/wiki/Uncanny_X-Men_Vol_1_{issue}"
            ).text
            soup = BeautifulSoup(html, "html.parser")
            for elt in soup.find_all("img", class_="pi-image-thumbnail"):
                source = elt.get("src")
                fobj.write(f"wget {source}\n")
                print(f"wrote source {source}")


if __name__ == "__main__":
    exit(main())
