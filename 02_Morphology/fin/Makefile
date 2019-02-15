all:
	hfst-lexc fin.lexc -o fin.lexc.hfst
	hfst-twolc fin.twol -o fin.twol.hfst
	hfst-compose-intersect -1 fin.lexc.hfst -2 fin.twol.hfst -o fin.gen.hfst
	hfst-minimise fin.gen.hfst | hfst-fst2txt | python3 att2dot.py | dot -Tpng -ofin.gen.png
	open fin.gen.png
