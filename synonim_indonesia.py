import re, pandas as pd
import pandasql as ps
import random


text = """
Sudah lebih dari 9 bulan sejak kasus pertama covid-19 ditemukan di Indonesian. Pandemi virus Corona yang mewabah berimbas pada segala bidang tidak terkecuali pada bidang pendidikan yang pada akhirnya kegiatan pembelajaran di sekolah dihentikan dan diganti dengan pembelajaran daring/ online

Proses pembelajaran secara daring yang dilakukan di rumah akan berjalan dengan baik jika peserta didik dapat mengatur dirinya dengan baik. Jika tidak demikian maka proses belajar daring yang dilakukan di rumah akan bergeser pada hal-hal yang kurang bermanfaat atau berbahaya seperti main game, browsing hal-hal negatif, bahkan sampai tindak kekerasan yang dilakukan oleh orang tua terhadap anaknya.
"""

list_txt = [x.replace('\n', '').replace('.', '').replace(',', '') for x in text.split(" ")]
random_list_txt = random.sample(list_txt, round(len(list_txt)/2))
with open('/Users/ayyoub/de_project/Daftar-Antonim-Tesaurus-Bahasa-Indonesia/tesaurus-id.txt', 'r') as f:
    lines = f.readlines()
    
lines_clear = [[re.sub(r'\d\,\s',',', y) for y in re.sub(r'^\-.*|^\d|(\;|)\n$|\d+\s+|\d+', '', re.sub(r'(\s|^)(n|v|p|a|pron|adv)\s', ', ', x.replace('- ',''))).split('; ') if y] for x in lines]
df_sin = pd.DataFrame(lines_clear)
df_sin = df_sin.rename(columns={0:'word'})[['word']]

for w in random_list_txt:
    try:
        syn = ps.sqldf(f"select word from df_sin where word like '{w},%' or word like '%,{w}' or word like '%, {w}' or word like '%,{w},%' or word like '%, {w},%'")
        sample = syn.sample(1)['word']
        print(sample)
        selected = random.choice(sample[sample.index[0]].split(", "))
        text = text.replace(w, selected)
    except Exception as e:
        print(str(e))
