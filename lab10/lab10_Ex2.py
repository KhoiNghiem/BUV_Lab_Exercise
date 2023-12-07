import json
import pandas as pd

file_path = 'char_classes.json'

with open(file_path, 'r') as file:
    data = json.load(file)

table_headers = ["Class", "Strength", "Intelligence", "Wisdom", "Dexterity", "Constitution"]
table_rows = []

for class_name, attributes in data.items():
    row = [class_name.capitalize()]
    for attr in ["str", "int", "wis", "dex", "con"]:
        row.append(attributes.get(attr, "-"))
    table_rows.append(row)


df = pd.DataFrame(table_rows, columns=table_headers)

final_df = df.style.set_properties(**{'text-align': 'center'}).apply(lambda x: ["text-align: left" if x.name == 'Class' else '' for _ in x], axis=0)

final_df.set_table_styles({
    'Class': [{'selector': 'th', 'props': [('text-align', 'left')]},
              {'selector': 'td', 'props': [('text-align', 'left')]}],
    }, overwrite=False, axis=0)

final_df