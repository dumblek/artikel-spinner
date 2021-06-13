#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 16:21:54 2021

@author: ayyoub
"""

import re, pandas as pd
import pandasql as ps

with open('/Users/ayyoub/de_project/Daftar-Antonim-Tesaurus-Bahasa-Indonesia/tesaurus-id.txt', 'r') as f:
    lines = f.readlines()
    
lines_clear = [[re.sub(r'\d\,\s',',', y) for y in re.sub(r'^\-.*|^\d|(\;|)\n$|\d+\s+', '', re.sub(r'\s(n|v|p|a|pron)\s', ', ', x.replace('- ',''))).split('; ') if y] for x in lines]
df_sin = pd.DataFrame(lines_clear)
df_sin = df_sin.rename(columns={0:'word'})[['word']]

ps.sqldf("select word from df_sin where word like 'bengkok,%' or word like '%,bengkok' or word like '%, bengkok' or word like '%,bengkok,%' or word like '%, bengkok,%'")