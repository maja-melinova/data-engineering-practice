import requests
import os
import pandas as pd
import re
import csv


def main():
    if not os.path.exists("data"):
        os.makedirs("data")

    uri = "https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/"
    r = requests.get(uri)

    if r.ok:
        web_text = r.text
        split_text = web_text.split("</a>")


        #Dataset, který by podle zadání měl byt Last Modified tam vůbec není (nejdřívější čas je 14:47)
        #Pro ukázku budu vyhledávat dataset o velikosti např. 4717710 (protože je jediný)

        for i in split_text:
            if i.find("4717710") != -1: #zde by se případně dalo zadat i "2024-01-19 10:27" podle zadání
                right_element = i

        name = re.search(r'a href="(.*?)\.csv"', right_element)
        csv_name = name.group(1) + ".csv"
        dataframe = pd.read_csv(uri + csv_name)
        dataframe.to_csv('data/data.csv')

        print(dataframe[dataframe['HourlyDryBulbTemperature'] == dataframe['HourlyDryBulbTemperature'].max()])

    pass


if __name__ == "__main__":
    main()
