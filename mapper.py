import sys
from urllib.parse import unquote_plus
import re

ignore_prefixes = [
    "Media",
    "Special",
    "Talk",
    "User",
    "User_talk",
    "Project",
    "Project_talk",
    "File",
    "File_talk",
    "MediaWiki",
    "MediaWiki_talk",
    "Template",
    "Template_talk",
    "Help",
    "Help_talk",
    "Category",
    "Category_talk",
    "Portal",
    "Wikipedia",
    "Wikipedia_talk",
]

ignore_suffixes = [
    ".jpg",
    ".gif",
    ".png",
    ".JPG",
    ".GIF",
    ".PNG",
    ".ico",
    ".txt",
]

# TODO: figure this out
ignore_pages = ["404_error", "Main_Page", "Hypertext_Transfer_Protocol", "Search"]

for entry in map(str.rstrip, sys.stdin):
    project_code, page_name, page_views, size = entry.split(" ")

    page_name = page_name.replace("%0A", "")
    page_name = unquote_plus(page_name)
    page_name = page_name.replace("_", " ")

    skip = not project_code.startswith("en") or re.match(r"^[A-Z].*", page_name) is None

    for prefix in ignore_prefixes:
        if page_name.startswith(prefix):
            skip = True
            break

    for suffix in ignore_suffixes:
        if page_name.endswith(suffix):
            skip = True
            break

    if skip:
        continue

    print(page_name, page_views, sep="\t")
