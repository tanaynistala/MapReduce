gzcat data/20160601/* | python3 mapper.py > output/map_20160601.tsv
gzcat data/20160602/* | python3 mapper.py > output/map_20160602.tsv
cat output/map_20160601.tsv output/map_20160602.tsv | LC_ALL=C sort -k 1 | python3 reducer.py > output/reducer.tsv