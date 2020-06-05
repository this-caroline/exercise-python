#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd

xlsx = pd.ExcelFile("file.xlsx")
df = pd.read_excel(xlsx,'Planilha1')

data = df[[df.columns[3],df.columns[1]]]

consumeM = 0
consumeF = 0
for index, row in data.iterrows():
    if(row[df.columns[1]] == 'M'):
        consumeM = consumeM + row[df.columns[3]]
    if (row[df.columns[1]] == 'F'):
        consumeF = consumeF + row[df.columns[3]]

if(consumeF < consumeM):
    print('O gênero mais sóbrio é o feminino')

if(consumeM < consumeF):
    print('O gênero mais sóbrio é o masculino')
