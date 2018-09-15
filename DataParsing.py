import pandas as pd


def main():
chemicalDf = pd.read_excel("./storetLabeled.xlsx")
mainDf = pd.read_excel("./chemical.xlsx")
watsysDf = pd.read_csv("./watsys.csv", encoding='cp1252')
sitelocDf = pd.read_csv("./siteloc.csv")


main()