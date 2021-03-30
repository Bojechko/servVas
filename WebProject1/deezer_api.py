import deezer
import json


client = deezer.Client()

def  get_band_albums(band):
   albums=client.search(band, relation='artist')[0].get_albums() #ищем альбомы
   
   dict_of_albums = { i :{ albums[i].title  : {albums[i].id : albums[i].cover}} for i in range(0, len(albums))}#берем у каждого найденного альбома id, название

   return json.dumps(dict_of_albums)

def  get_album(band, album):
   albums=client.search(band, relation='artist')[0].get_albums() #ищем альбомы
   inc = 0 
   while inc< len(albums):
       
       if albums[inc].title == album :
            return inc
       inc += 1 
   return "No album found"


   
   

def  get_albums_tracks(band, album):
   tracks=client.search(band, relation='artist')[0].get_albums()[get_album(band, album)].get_tracks() #ищем треки
   #print(client.search(band, relation='artist')[0].get_albums()[album].get_tracks())
   dict_of_tracks = {  tracks[i].title : { tracks[i].id : tracks[i].link} for i in range(0, len(tracks))}#берем у каждого найденного трека id, название
   return json.dumps(dict_of_tracks)

    