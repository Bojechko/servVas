import deezer
import json


client = deezer.Client()

def  get_band_albums(band):
   try :
        albums=client.search(band, relation='artist')[0].get_albums() #ищем альбомы
   
        dict_of_albums = { i :{ albums[i].title  : {albums[i].id : albums[i].cover}} for i in range(0, len(albums))}#берем у каждого найденного альбома id, название
   
        return json.dumps(dict_of_albums)
   except Exception : 
        return "No such band, error in get_band_albums"


def  get_album(band, album):
   albums=client.search(band, relation='artist')[0].get_albums() #ищем альбом
   inc = 0 
   while inc< len(albums):
       
       if albums[inc].title == album :
            return inc
       inc += 1 
   return "No album found"


   
   

def  get_albums_tracks(band, album):
    try:
        tracks=client.search(band, relation='artist')[0].get_albums()[get_album(band, album)].get_tracks() #ищем треки
        dict_of_tracks = {  tracks[i].title : { tracks[i].id : tracks[i].link} for i in range(0, len(tracks))}#берем у каждого найденного трека id, название
        return json.dumps(dict_of_tracks)
    except Exception : 
        return "No such album, error in get_albums_tracks"

    