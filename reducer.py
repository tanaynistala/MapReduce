import sys

current_name = None
current_count = 0

for entry in map(str.rstrip, sys.stdin):
    page_name, count = entry.split("\t")

    if current_name == page_name:
        current_count += int(count)
    else:
        if current_name is not None:
            print(current_name, current_count, sep="\t")

        current_name = page_name
        current_count = int(count)

print(current_name, current_count, sep="\t")
