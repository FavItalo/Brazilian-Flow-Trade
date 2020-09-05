import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

ipea_flux = pd.read_excel(r'C:\Users\Italo\Dropbox\EESP\CEMAP\IPEA Data\IPEA fluxo de comercio.xlsx')

Chinac = []
Euaac = []
UniEupac = []
MercSulac = []
Afriac = []
Outac = []

for i in range(0,len(ipea_flux)):
    Chinac.append(ipea_flux.loc[i-12:i,'China'])
    Euaac.append(ipea_flux.loc[i-12:i,'EUA'])
    UniEupac.append(ipea_flux.loc[i-12:i,'EU'])
    MercSulac.append(ipea_flux.loc[i-12:i,'Mercs'])
    Afriac.append(ipea_flux.loc[i-12:i,'Africa'])
    Outac.append(ipea_flux.loc[i-12:i,'Outros'])

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

ipea_flux['China'] = dfsChinacl['China']
ipea_flux['EUA'] = dfsEuaacl['EUA']
ipea_flux['EU'] = dfsUniEupacl['EU']
ipea_flux['Mercs'] = dfsMercSulacl['Mercs']
ipea_flux['Africa'] = dfsAfriacl['Africa']
ipea_flux['Outros'] = dfsOutacl['Outros']

for row in ipea_flux.index:
    labels = ['China', 'USA', 'MercoSul', 'Europe', 'Africa', 'RoW']
    sizes = ipea_flux.loc[row, 'China':'Outros']
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, autopct='%1.f%%', shadow=False, startangle=90)
    ax1.axis('equal')
    plt.legend(labels, loc=0)
    ax1.set_title('Share of each partner in Brazil\'s Total Trade Flows – ' + str(ipea_flux.loc[row,'Year']))
    plt.savefig(r'C:\Users\Italo\Dropbox\EESP\CEMAP\IPEA Data\graphs flux com\graph' + str(ipea_flux.loc[row,'Data']) + '.png', dpi=200)
