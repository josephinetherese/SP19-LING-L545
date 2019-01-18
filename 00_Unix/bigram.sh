#!bin/bash
# January 17, 2019
# Josephine Douglas

gsed 's/[^a-zA-Z]\+/\n/g' | grep -v '^$' > $$_words
tail -n +2 $$_words > $$_nextwords
paste $$_words $$_nextwords | sort | uniq -c
rm $$_words $$_nextwords
