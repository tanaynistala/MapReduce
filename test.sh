gzcat data/20160603/* | python3 mapper.py > output/map_20160603.tsv
gzcat data/20160604/* | python3 mapper.py > output/map_20160604.tsv
cat output/map_20160603.tsv output/map_20160604.tsv | LC_ALL=C sort -k 1 | python3 reducer.py > output/reducer_test.tsv