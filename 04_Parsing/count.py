
import argparse
HOME = "/Users/josephinedouglas/SPRING_2019/SP19-LING-L545/misc/"
V = []
O = []
files = []
def count_order(filename, c):
    lines = []
    with open (HOME+filename, 'r') as f:
      lines = f.readlines()

    root = -1;
    object = -1;
    VO = 0;
    OV = 0;
    for current in lines:
        columns = current.split('\t')
        if len(columns) > 8:
            #columns[7] obj (HINDI)
            if columns[c] == "0":
                root = columns[0]
            elif columns[c] == root and "obj" in columns[c+1]:
                object = columns[0]
            if root != -1 and object != -1:
                if root > object:
                    OV += 1
                else:
                    VO += 1
    total = VO + OV
    V.append(VO/total)
    O.append(OV/total)
    files.append(filename.split('/')[-2])
    # print(filename.split('/')[-2],VO/total, OV/total)

def runAll():
    count_order("UD_Finnish-TDT/fi_tdt-ud-train.conllu", 6)
    count_order("UD_Portuguese-GSD/pt_gsd-ud-train.conllu", 6)
    count_order("UD_Swedish-Talbanken/sv_talbanken-ud-train.conllu", 6)
    count_order("UD_Hindi-HDTB/hi_hdtb-ud-train.conllu", 6)
    count_order("UD_Croatian-SET/hr_set-ud-train.conllu", 6)
    count_order("UD_English-LinES/en_lines-ud-train.conllu", 6)
    count_order("UD_German-GSD/de_gsd-ud-train.conllu", 6)
    count_order("UD_Hindi_English-HIENCS/qhe_hiencs-ud-train.conllu", 6)
    count_order("UD_Polish-LFG/pl_lfg-ud-train.conllu", 6)
    count_order("UD_Russian-SynTagRus/ru_syntagrus-ud-train.conllu",6)
    count_order("UD_Turkish-IMST/tr_imst-ud-test.conllu",6)

# parses command line arguments
def get_argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", help="conll file to read")
    # parser.add_argument("-c", help="column with dependencies", type=int)
    return parser

def main():
    parser = get_argparser()
    args = parser.parse_args()
    # count_order(args.f, 6)
    runAll()
    print(files,V,O)

if __name__ == '__main__':
    main()
