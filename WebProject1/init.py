from typing import Optional
from fastapi import FastAPI
import deezer_api as api

app = FastAPI()


@app.get("/get_albums/{band}")
def get_albums(band):
    try:
        return api.get_band_albums(band) 
    except BaseException: 
        return "No such band"
            

@app.get("/get_albums/{band}/{album}")
def get_tracks(band, album):
    try:
        return  api.get_albums_tracks(band, int(album))
    except BaseException: 
        return "No such album"

