import requests
import os
import zipfile
import io

download_uris = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip",
]

def main():

    if not os.path.exists("downloads"):
        os.makedirs("downloads")

    for uri in download_uris:
        r = requests.get(uri)

        if r.ok:
            name = os.path.split(uri)[1]
            name = name.removesuffix('.zip')

            z = zipfile.ZipFile(io.BytesIO(r.content))
            #z.extractall("downloads")
            z.extract(name+".csv", "downloads")

    pass


if __name__ == "__main__":
    main()
