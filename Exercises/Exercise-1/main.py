import requests
import os
import zipfile
import io
from concurrent.futures import ThreadPoolExecutor
import asyncio
import aiohttp

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
            #print(z.namelist())
            z.extract(name + ".csv", "downloads")

    # ------------------------------------------------------------
    # aiohttp
    # ------------------------------------------------------------
    if not os.path.exists("downloads/aiohttp"):
        os.makedirs("downloads/aiohttp")

    async def download_aiohttp(uri):
        r = requests.get(uri)

        if r.ok:
            name = os.path.split(uri)[1]
            name = name.removesuffix('.zip')

            z = zipfile.ZipFile(io.BytesIO(r.content))
            z.extract(name + ".csv", "downloads/aiohttp")

    async def fce():
        tasks = [download_aiohttp(uri) for uri in download_uris]
        await asyncio.gather(*tasks)

    asyncio.run(fce())

    #------------------------------------------------------------
    #ThreadPoolExecutor
    #------------------------------------------------------------
    if not os.path.exists("downloads/ThreadPoolExecutor"):
        os.makedirs("downloads/ThreadPoolExecutor")

    def download_threadpool(uri):
        r = requests.get(uri)

        if r.ok:
            name = os.path.split(uri)[1]
            name = name.removesuffix('.zip')

            z = zipfile.ZipFile(io.BytesIO(r.content))
            z.extract(name + ".csv", "downloads/ThreadPoolExecutor")

    with ThreadPoolExecutor() as executor:
        executor.map(download_threadpool, download_uris)

    pass

if __name__ == "__main__":
    main()
