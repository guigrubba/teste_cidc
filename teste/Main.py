import pandas as pd
import numpy as np

#Puxando arquivos e obtendo os dataFrames
results = pd.read_excel('arquivos/Results.xlsx')
siteList = pd.read_excel('arquivos/SiteList.xlsx')

#Mesclando os DataFrames
report = pd.merge(siteList, results, how='outer')

#Ordenando por Estados
report = report.sort_values('State')


#Exportando o arquivo
report.to_excel("report/quality-report-2023.xlsx", index=False)

#Exibir sites com alertas ativos
alerts = results["Alerts"]
num_indices = results.size






