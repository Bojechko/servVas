from modules.deezer_api import get_album_img
from unittest.mock import patch


# Regular test
def test_get_album_img():
    assert get_album_img('System of a Down', 'Toxicity') == "http://stackoverflow.com"


# Test with mocked response from internal call
@patch('modules.deezer_api.json.loads')
def test_get_mocked_album_img(mock):
    mock.return_value = {'Tool': {'Lateralus': {'id': 789, 'img': 'http://reddit.com'}}}
    assert get_album_img('Tool', 'Lateralus') == 'http://reddit.com'
