import json

data = []
with open('convert.txt', encoding='utf-8') as f:
    data = f.readlines()

no_tabs = [i.replace('\t', ' ').strip() for i in data]
group = []
groups = []

for line in no_tabs:
    if line:
        group.append(line)
    else:
        groups.append(group)
        group = []
if group:
    groups.append(group)
    group = []

objs = []
for group in groups:
    obj = {}
    obj['players'] = group[0].split(" ")
    obj['total'] = group[1].split(" ")
    obj['round_1'] = group[2].split(" ")
    obj['round_2'] = group[3].split(" ")
    obj['round_3'] = group[4].split(" ")
    obj['round_4'] = group[5].split(" ")
    obj['round_5'] = group[6].split(" ")
    obj['round_6'] = group[7].split(" ")
    obj['round_7'] = group[8].split(" ")
    objs.append(obj)

with open('db.json', 'w', encoding='utf-8') as f:
    json.dump(objs, f, indent=4, separators=(',', ": "))