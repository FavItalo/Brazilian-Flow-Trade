import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

ipea_exp = pd.read_excel(r'C:\Users\Italo\Dropbox\EESP\CEMAP\IPEA Data\IPEA Exp py.xlsx')

Chinac = []
Euaac = []
UniEupac = []
MercSulac = []
Afriac = []
Outac = []

for i in range(0,len(ipea_exp)):
    Chinac.append(ipea_exp.loc[i-12:i,'China'])
    Euaac.append(ipea_exp.loc[i-12:i,'EUA'])
    UniEupac.append(ipea_exp.loc[i-12:i,'EU'])
    MercSulac.append(ipea_exp.loc[i-12:i,'Mercs'])
    Afriac.append(ipea_exp.loc[i-12:i,'Africa'])
    Outac.append(ipea_exp.loc[i-12:i,'Outros'])

Chinacl = []
Euaacl = []
UniEupacl = []
MercSulacl = []
Afriacl = []
Outacl = []
for i in range(0,len(Chinac)):
    Chinacl.append(Chinac[i].tolist())
    Euaacl.append(Euaac[i].tolist())
    UniEupacl.append(UniEupac[i].tolist())
    MercSulacl.append(MercSulac[i].tolist())
    Afriacl.append(Afriac[i].tolist())
    Outacl.append(Outac[i].tolist())

sChinacl = []
sEuaacl = []
sUniEupacl = []
sMercSulacl = []
sAfriacl = []
sOutacl = []
for i in range(0,len(Chinacl)):
    sChinacl.append(sum(Chinacl[i]))
    sEuaacl.append(sum(Euaacl[i]))
    sUniEupacl.append(sum(UniEupacl[i]))
    sMercSulacl.append(sum(MercSulacl[i]))
    sAfriacl.append(sum(Afriacl[i]))
    sOutacl.append(sum(Outacl[i]))

dfsChinacl = pd.DataFrame(sChinacl)
dfsChinacl.columns = ['China']
dfsEuaacl = pd.DataFrame(sEuaacl)
dfsEuaacl.columns = ['EUA']
dfsUniEupacl = pd.DataFrame(sUniEupacl)
dfsUniEupacl.columns = ['EU']
dfsMercSulacl = pd.DataFrame(sMercSulacl)
dfsMercSulacl.columns = ['Mercs']
dfsAfriacl = pd.DataFrame(sAfriacl)
dfsAfriacl.columns = ['Africa']
dfsOutacl = pd.DataFrame(sOutacl)
dfsOutacl.columns = ['Outros']

ipea_exp['China'] = dfsChinacl['China']
ipea_exp['EUA'] = dfsEuaacl['EUA']
ipea_exp['EU'] = dfsUniEupacl['EU']
ipea_exp['Mercs'] = dfsMercSulacl['Mercs']
ipea_exp['Africa'] = dfsAfriacl['Africa']
ipea_exp['Outros'] = dfsOutacl['Outros']

for row in ipea_exp.index:
    labels = ['China', 'USA', 'MercoSul', 'Europe', 'Africa', 'RoW']
    sizes = ipea_exp.loc[row, 'China':'Outros']
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, autopct='%1.f%%', shadow=False, startangle=90)
    ax1.axis('equal')
    plt.legend(labels, loc=0)
    ax1.set_title('Share of each partner in Brazilian Total Exports over the years – ' + str(ipea_exp.loc[row,'Data']))
    plt.savefig(r'C:\Users\Italo\Dropbox\EESP\CEMAP\IPEA Data\graphs exp\graph' + str(ipea_exp.loc[row,'year']) + '.png', dpi=200)

