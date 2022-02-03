import requests
import json

# https://www.datamuse.com/api/ ###todo sobre APIS
page = requests.get('https://www.google.com/search?tbm=isch&q=%22violins+and+guitars%22')


parameters = {"term": "Ann Arbor", "entity": "podcast"}
iTunes_response = requests.get("https://itunes.apple.com/search", params = parameters)
py_data = json.loads(iTunes_response.text)

pyDataString = str(py_data)
print(pyDataString)

def get_flickr_data(tags_string):
    baseurl = "https://api.flickr.com/services/rest/"
    params_diction = {}
    params_diction["api_key"] = 'c92554a696c5d98d678156e0620d5b45' # from the above global variable
    params_diction["tags"] = tags_string # must be a comma separated string to work correctly
    params_diction["tag_mode"] = "all"
    params_diction["method"] = "flickr.photos.search"
    params_diction["per_page"] = 5
    params_diction["media"] = "photos"
    params_diction["format"] = "json"
    params_diction["nojsoncallback"] = 1
    flickr_resp = requests.get(baseurl, params = params_diction)

    print(flickr_resp.url)

    return flickr_resp.json()

result = get_flickr_data('river,mountains')

print(result.keys())
print(result['photos'])

data_res = result['photos']

for i in data_res['photo']:

    print(i.keys())
    print('Owner = {}, server = {}, title = {}'.format(i['owner'],i['server'],i['title']))
    owner = i['owner']
    photo_id = i['id']
    url = 'https://www.flickr.com/photos/{}/{}'.format(owner,photo_id)
    print(url)
