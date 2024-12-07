gzcat data/20160603/* | python3 mapper.py > output/map_20160603.txt
gzcat data/20160604/* | python3 mapper.py > output/map_20160604.txt
cat output/* | sort -n -k 1 | python3 reducer.py > reducer_output.txt