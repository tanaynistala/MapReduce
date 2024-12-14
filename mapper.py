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


def remove_control_characters(s):
    import unicodedata

    return "".join(ch for ch in s if unicodedata.category(ch)[0] != "C")


for entry in map(str.rstrip, sys.stdin):
    project_code, page_name, page_views, size = entry.split(" ")

    # Clean page names and remove non-ASCII and control characters
    page_name = remove_control_characters(unquote_plus(page_name))

    # Exclude pages
    if any(
        [
            # Exclude non-English pages
            not project_code.startswith("en"),
            # Exclude pages without uppercase initial
            re.match(r"^[A-Z].*", page_name) is None,
            # Exclude prefixes
            any([page_name.startswith(prefix) for prefix in ignore_prefixes]),
            # Exclude suffixes
            any([page_name.startswith(suffix) for suffix in ignore_suffixes]),
            # Exclude boilerplate
            any([page_name == page for page in ignore_pages]),
        ]
    ):
        continue

    print(page_name, page_views, sep="\t")
