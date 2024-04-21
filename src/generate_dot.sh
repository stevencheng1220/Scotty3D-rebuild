#!/bin/bash
echo "digraph G {"
for i in $(find . -name '*.cpp' -or -name '*.h'); do
    for j in $(grep '#include' $i | sed -e 's/#include //g' -e 's/"//g' -e 's/<//g' -e 's/>//g'); do
        # You may need additional processing here to trim paths, resolve relative paths, etc.
        echo "\"$(basename $i)\" -> \"$j\";"
    done
done
echo "}"
