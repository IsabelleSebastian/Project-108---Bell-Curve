import pandas 
import plotly.figure_factory as pe
import csv

df = pandas.read_csv("company.csv")
data = df["Avg Rating"].tolist()
graph = pe.create_distplot([data], ["Average Rating Plot"])
graph.show()