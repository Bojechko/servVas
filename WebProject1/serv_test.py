
import init
import deezer_api
import pytest


# init tests
def test_get_albums():
    assert init.get_albums('Korn') != 'No such band'

def test_get_albums2():
    assert init.get_albums('ssadsadd') == 'No such band'

def test_get_albums3():
    assert init.get_albums(' ') == 'No such band'

def test_get_albums4():
    assert init.get_albums('') == 'No such band'



def test_get_tracks():
    assert init.get_tracks('Korn', 'The Nothing') != 'No such album'

def test_get_tracks2():
    assert init.get_tracks('Korn', 'ф фыв') == 'No such album'

def test_get_tracks3():
    assert init.get_tracks('фывфывфы', 'The Nothing') == 'No such album'

def test_get_tracks4():
    assert init.get_tracks('', '') == 'No such album'

def test_get_tracks5():
    assert init.get_tracks('Korn', '') == 'No such album'


#deezer_api tests

def test_get_album():
    assert deezer_api.get_album('Korn', 'The Nothing') != "No album found"

def test_get_album2():
    assert deezer_api.get_album('Korn', 'asdasd') == "No album found"



