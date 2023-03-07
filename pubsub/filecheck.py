# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.14.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
import pandas as pd
import datetime
import statistics

# %%
filename = input('filename:')
df = pd.read_csv(filename, encoding='shift-jis',dtype= 'object')
df[df.columns[4]] = df[df.columns[4]].astype(int)
print(df[df.columns[4]])
print(df)

# %%
df[df.columns[0]] = pd.to_datetime(df[df.columns[0]])

# %%
print((df[df.columns[0]]))

# %%
allmsdata = df[(df[df.columns[0]] > (pd.to_datetime("2023/03/06 18:07:19"))) & (df[df.columns[0]] < (pd.to_datetime("2023/03/06 18:30:00")))]
print(allmsdata)

# %%
tagnum = 0
testlist = []
for tag in allmsdata.groupby(df.columns[2]):
    print(tag[0])
    tagdata = tag[1]
    datanums = tagdata[tagdata.columns[4]]
    ideal = datanums.max()-datanums.min()
    actual = len(datanums)
    #print (actual/ideal)
    testlist.append(actual/ideal)
    tagnum += 1
print('number of tag:' + str(tagnum))
print(statistics.mean(testlist))

# %%
