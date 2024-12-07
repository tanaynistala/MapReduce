gzcat data/20160601/* | python3 mapper.py > output/map_20160601.txt
gzcat data/20160602/* | python3 mapper.py > output/map_20160602.txt
cat output/* | sort -n -k 1 | python3 reducer.py > reducer_output.txt