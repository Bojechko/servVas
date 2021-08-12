
import init
import deezer_api
import deezer
import pytest
import unittest
from unittest.mock import patch



# init tests
'''def test_get_albums():
    assert init.get_albums('Korn') != 'No such band, error in get_band_albums'

def test_get_albums2():
    assert init.get_albums('ssadsadd') == 'No such band, error in get_band_albums'

def test_get_albums3():
    assert init.get_albums(' ') == 'No such band, error in get_band_albums'

def test_get_albums4():
    assert init.get_albums('') == 'No such band, error in get_band_albums'




def test_get_tracks():
    assert init.get_tracks('Korn', 'The Nothing') != 'No such album, error in get_albums_tracks'

def test_get_tracks2():
    assert init.get_tracks('Korn', 'ф фыв') == 'No such album, error in get_albums_tracks'

def test_get_tracks3():
    assert init.get_tracks('фывфывфы', 'The Nothing') == 'No such album, error in get_albums_tracks'

def test_get_tracks4():
    assert init.get_tracks('', '') == 'No such album, error in get_albums_tracks'

def test_get_tracks5():
    assert init.get_tracks('Korn', '') == 'No such album, error in get_albums_tracks'


#deezer_api tests

def test_get_album():
    assert deezer_api.get_album('Korn', 'The Nothing') != "No album found"

def test_get_album2():
    assert deezer_api.get_album('Korn', 'asdasd') == "No album found"
    
def test_get_album3():
    assert deezer_api.get_album('Korn', 'The Nothing') == 0



def test_get_band_albums():
    assert deezer_api.get_band_albums('Korn') != "No such band, error in get_band_albums"
    
def test_get_band_albums2():
    assert deezer_api.get_band_albums(' ') == "No such band, error in get_band_albums"
    
def test_get_band_albums3():
    assert deezer_api.get_band_albums('')  == "No such band, error in get_band_albums"

def test_get_band_albums4():
    assert deezer_api.get_band_albums('точно не существет')  == "No such band, error in get_band_albums"


def test_get_albums_tracks():
    assert deezer_api.get_albums_tracks('Korn', 'The Nothing') != "No such album, error in get_albums_tracks"
    
def test_get_albums_tracks2():
    assert deezer_api.get_albums_tracks(' ', ' ') == "No such album, error in get_albums_tracks"
    
def test_get_albums_tracks3():
    assert deezer_api.get_albums_tracks('', '')  == "No such album, error in get_albums_tracks"

def test_get_albums_tracks4():
    assert deezer_api.get_albums_tracks('точно не существет', 'этого тоже нет')  == "No such album, error in get_albums_tracks"

def test_get_albums_tracks6():
    assert deezer_api.get_albums_tracks('Korn', '') == "No such album, error in get_albums_tracks"

def test_get_albums_tracks7():
    assert deezer_api.get_albums_tracks('Korn', ' ') == "No such album, error in get_albums_tracks"

def test_get_albums_tracks8():
    assert deezer_api.get_albums_tracks('', 'The Nothing') == "No such album, error in get_albums_tracks"

def test_get_albums_tracks9():
    assert deezer_api.get_albums_tracks('Korn', 'точно не существет') == "No such album, error in get_albums_tracks"

def test_get_albums_tracks9():
    assert deezer_api.get_albums_tracks('точно не существет', 'The Nothing') == "No such album, error in get_albums_tracks"
'''

    #mock------------------------------------------------------------------------------------------------------

class Test_get_band_albums(unittest.TestCase):
    Hypnotize = "{\"0\": {\"Hypnotize\": {\"1442650\": \"https://api.deezer.com/album/1442650/image\"}}"

    @patch( "deezer_api.client.search(band, relation='artist')[0].get_albums()" , return_value = "{\"0\": {\"Hypnotize\": {\"1442650\": \"https://api.deezer.com/album/1442650/image\"}}")
    def test_get_band_albums_correct(self):      
        assert get_band_albums('system of a down') == json.dumps(Hypnotize)
    







