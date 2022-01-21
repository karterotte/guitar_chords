import prettytable as pt
import numpy as np
import random

use_jp = False
df_scale = "----"
df_fileds = ['⓪','①','②','③','④','⑤','⑥','⑦','⑧','⑨','⑩','⑪','⑫']
df_row = [df_scale] * 13 * 6
df_table = np.array(df_row).reshape(6, 13)

scale_json={
    "A2":[(4,0),(5,5)],
    "B2":[(4,2),(5,7)],
    "E2":[(5,0)],
    "F2":[(5,1)],
    "G2":[(5,3)],
    "A3":[(2,2),(3,7),(4,12)],
    "B3":[(1,0),(2,4),(3,9)],
    "C3":[(4,3),(5,8)],
    "D3":[(3,0),(4,5),(5,10)],
    "E3":[(3,2),(4,7),(5,12)],
    "F3":[(3,3),(4,8)],
    "G3":[(2,0),(3,5),(4,10)],
    "A4":[(0,5),(1,10)],
    "B4":[(0,7),(1,12)],
    "C4":[(0,8),(1,1),(2,5),(3,10)],
    "D4":[(1,3),(2,7),(3,12)],
    "E4":[(0,0),(1,5),(2,9)],
    "F4":[(0,1),(1,6),(2,10)],
    "G4":[(0,3),(1,8),(2,12)],
    "D5":[(0,10)],
    "E5":[(0,12)]
}

jp_json = {
    "C": "1",
    "D": "2",
    "E": "3",
    "F": "4",
    "G": "5",
    "A": "6",
    "B": "7"
}

def make_table(scale_table):
    tb = pt.PrettyTable()
    tb.field_names = df_fileds
    for row in scale_table:
        if use_jp:
            tb.add_row([' '+jp_json[s[0]]+' ' if s!=df_scale else '---' for s in row])
        else:
            tb.add_row([' '+s+' ' if s!=df_scale else s for s in row])
    tb.border = True
    return tb

def random_scale(scale_table, num=1):
    keys = list(scale_json.keys())
    rkeys =[]
    for idx in range(num):
        s = random.choice(keys)
        rkeys.append(s)
        for pos in scale_json[s]:
            scale_table[pos]=s
    print(rkeys)
    return scale_table

def random_scale(scale_table):
    s = random.choice(['A','B','C','D','E','F','G'])
    print(s)
    for k,v in scale_json.items():
        if k.startswith(s):
            for pos in v:
                scale_table[pos]=k
    return scale_table

def collect_scale(scale_table, show_rows=[], show_fields=[]):
    for s,v in scale_json.items():
        for pos in v:
            if (not show_rows or (show_rows and pos[0] in show_rows) ) and \
                (not show_fields or (show_fields and pos[1] in show_fields)):
                scale_table[pos]=s
    return scale_table

def show_all():
    scale_table = df_table
    print(make_table(collect_scale(scale_table)))

def show_scale_1():
    scale_table = df_table
    print(make_table(collect_scale(scale_table, show_fields=list(range(6)))))

def show_scale_2():
    scale_table = df_table
    print(make_table(collect_scale(scale_table, show_fields=list(range(5,11)))))

def show_random_1():
    scale_table = df_table
    print(make_table(random_scale(scale_table,3)))

def show_random_2():
    scale_table = df_table
    print(make_table(random_scale(scale_table)))

if __name__ == '__main__':
    show_scale_1()
