import plotly.express as px
import csv
import numpy as np

def plotFigure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x="MarksInPercentage", y="DaysPresent")
        fig.show()

def getDataSource(data_path):
    marks = []
    present = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            marks.append(float(row["MarksInPercentage"]))
            present.append(float(row["DaysPresent"]))

    return {"x" : marks, "y": present}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("""Correlation between Marks obtained and Days Present is
        """,correlation[0,1])

def setup():
    data_path  = "StudentMarks.csv"

    datasource = getDataSource(data_path)
    findCorrelation(datasource)
    plotFigure(data_path)

setup()