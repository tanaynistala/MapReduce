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

ignore_pages = ["404_error", "Main_Page", "Hypertext_Transfer_Protocol", "Search"]

for entry in map(str.strip, sys.stdin):
    try:
        project_code, page_name, page_views, size = entry.split()

        # Exclude pages
        if any(
            [
                # Exclude non-English pages
                not project_code.startswith("en"),
                # Exclude pages without uppercase initial
                all(
                    [
                        ord(page_name[0]) < 128,
                        page_name[0].isalpha(),
                        page_name[0].islower(),
                    ]
                ),
                # Exclude prefixes
                any([page_name.startswith(prefix) for prefix in ignore_prefixes]),
                # Exclude suffixes
                any([page_name.endswith(suffix) for suffix in ignore_suffixes]),
                # Exclude boilerplate
                any([page in page_name for page in ignore_pages]),
            ]
        ):
            continue

        print(unquote_plus(page_name).replace("\t", ""), page_views, sep="\t")
    except:
        print(entry, file=sys.stderr)
