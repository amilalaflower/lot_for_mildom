import pandas as pd
import glob
import os

keyword = input("抽選キーワードを入力してください: ")
base_dir = os.path.dirname(os.path.abspath(__file__))
in_path = base_dir + '\chatdata\chatdata_*.log'
out_path = base_dir + '\結果.log'

csv_files = glob.glob(in_path)
data_list = []
for file in csv_files:
    data_list.append(pd.read_csv(file, encoding = "shift-jis", header=None, names=['time', 'name', 'comment']))

df = pd.concat(data_list, axis=0, sort=True)
namelist = df[df['comment'] == keyword]['name'].values.tolist()
unique_namelist = list(set(namelist))

text = "\n".join(unique_namelist)
with open(out_path, "w") as f:
    f.write(text)