# Maimoona Aziz

import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    # Check format and get video ID
    if matches := re.search(r'<iframe.*?src="https?://(?:www\.)?youtube\.com/embed/(.+?)".*?></iframe>', s):
        id = matches.group(1)
        # Combine link and ID
        link = "https://youtu.be/" + id

        return link


if __name__ == "__main__":
    main()
