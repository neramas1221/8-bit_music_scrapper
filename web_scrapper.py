import requests
from bs4 import BeautifulSoup
import time
import numpy as np
import pandas as pd
import re
import sys
import time
from tqdm import tqdm

if (len(sys.argv) >= 2):
    page_url   = sys.argv[1] #https://www.vgmusic.com/music/console/nintendo/gameboy/
    page       = requests.get(page_url)
    soup       = BeautifulSoup(page.text, 'lxml')
    table      = soup.find('table')
    a_herf     = table.find_all('a')
    files      = []
    output_loc = "/home/neramas1221/Git/video_game_music/8-bit/"

    print(len(a_herf))
    for i in tqdm(range(0,len(a_herf))):
        if(".mid" in str(a_herf[i])):
            href = a_herf[i]
            href = href['href']
            files.append(href)


    f = open("/home/neramas1221/Git/video_game_music/8-bit_files.txt", "a")
    for i in range(0,len(files)):
            f.write(output_loc+str(files[i]))
            f.write("\n")
    f.close()


    for i in tqdm(range(0,len(files))):
        url =  page_url+str(files[i])
        print(url)
        r   = requests.get(url, stream=True)
        with open(output_loc+str(files[i]), 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        f.close()
        time.sleep(1.0)


else:
    print("No URL provided")
    exit()