#bar based example on covid cases
import os
os.system('cls')
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import ScalarFormatter
covid = pd.read_excel('C:\\Users\\RIYA\\OneDrive\\Pictures\\Documents\\matplotlibdata.xlsx')
plt.figure(figsize=(10, 5))
country_labels = [country[:35] for country in covid['Country']]
plt.bar(country_labels[:35],covid['Cases'][:35])


plt.xlabel('Country')
plt.ylabel('Cases')
plt.title('Covid cases per country (Part 1)', fontdict={'fontname': 'Comic Sans Ms'})
plt.xticks( country_labels[:35],rotation=45,ha='right')  # Rotate x-axis labels for readability
plt.gca().yaxis.set_major_formatter(ScalarFormatter(useMathText=False))
plt.ticklabel_format(style='plain', axis='y')
plt.show()
# 2nd part of the graph
plt.figure(figsize=(10, 5))
bars=plt.bar(country_labels[35:], covid['Cases'][35:])
plt.xlabel('Country')
plt.ylabel('Cases')
plt.title('Covid cases per country (Part 2)', fontdict={'fontname': 'Comic Sans Ms'})
plt.xticks(rotation=45,ha='right')  # Rotate x-axis labels for readability
plt.gca().yaxis.set_major_formatter(ScalarFormatter(useMathText=False))
plt.ticklabel_format(style='plain', axis='y')
plt.show()
#Top 20 countries with max covid cases:
plt.figure(figsize=(10, 5))
top_n = 20
top_countries = covid.nlargest(top_n, 'Cases')
plt.bar(top_countries['Country'],top_countries['Cases'],color='blue')
plt.xlabel('Country')
plt.ylabel('Cases')
plt.title('COVID-19 Impact: Top Affected Countries by Cases ', fontdict={'fontname': 'Comic Sans Ms','fontsize':20})
plt.xticks(rotation=45 ,ha='right')
plt.gca().yaxis.set_major_formatter(ScalarFormatter(useMathText=False))
plt.ticklabel_format(style='plain', axis='y')
plt.show() 


