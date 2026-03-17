#!/usr/bin/env python3
"""
Check all external links in the content directory.
Reports broken or unreachable URLs.
"""

import os
import re
import sys
import urllib.request
import urllib.error
from pathlib import Path

CONTENT_DIR = "content"
URL_PATTERN = re.compile(r'https?://[^\s\)\]"\'<>]+')
TIMEOUT = 10

# URLs to skip (known-good or rate-limited)
SKIP_PATTERNS = [
    "localhost",
    "example.com",
]


def find_urls_in_file(filepath):
    urls = []
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    for match in URL_PATTERN.finditer(content):
        url = match.group(0).rstrip(".,;:)")
        if not any(skip in url for skip in SKIP_PATTERNS):
            urls.append((url, filepath))
    return urls


def check_url(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=TIMEOUT) as response:
            return response.status, None
    except urllib.error.HTTPError as e:
        return e.code, str(e)
    except Exception as e:
        return None, str(e)


def main():
    all_urls = []
    for root, _, files in os.walk(CONTENT_DIR):
        for filename in files:
            if filename.endswith(".md"):
                filepath = os.path.join(root, filename)
                all_urls.extend(find_urls_in_file(filepath))

    # Deduplicate
    seen = set()
    unique_urls = []
    for url, filepath in all_urls:
        if url not in seen:
            seen.add(url)
            unique_urls.append((url, filepath))

    print(f"Checking {len(unique_urls)} unique external URLs...")
    errors = []
    for url, filepath in unique_urls:
        status, error = check_url(url)
        if status is None or status >= 400:
            errors.append((url, filepath, status, error))
            print(f"  FAIL [{status}] {url} (in {filepath})")
        else:
            print(f"  OK   [{status}] {url}")

    if errors:
        print(f"\nFound {len(errors)} broken link(s).")
        sys.exit(1)
    else:
        print(f"\nAll {len(unique_urls)} links OK.")


if __name__ == "__main__":
    main()
