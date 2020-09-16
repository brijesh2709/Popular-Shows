# Functional Code


# return api function stores and returns the API key
def return_api() -> str:
    api = 'AIzaSyCVPQZGu2BL01mwz7nrZvKG8DNPPV5YDGo'
    return api


# make_url function creates a new url with desired
# parameters
def make_url(key: str) -> str:
    while True:
        url = 'https://www.googleapis.com/youtube/v3/videos?key='
        url += key + '&maxResults=5&chart=mostPopular&part=snippet%2C+'
        url += 'statistics&regionCode=us'
        if type(url) == str:
            return url
        else:
            continue

# make_request fuction passes on the url to make a request using
# the API key. The json library plays an important part in this


def make_request(url: str) -> {}:
    while True:
        # opens an url
        resp = urllib.request.urlopen(url)
        data = resp.read()
        # encodes the url for request
        text = data.decode(encoding = 'utf-8')
        # requests json 
        text = json.loads(text)
        if type(text) == dict:
            return text
        else:
            continue


# print_vid function prints the 5 trending videos
def print_vid(json_obj: dict):
    for item in json_obj['items']:
        print('Title     : ', item['snippet']['title'])
        print('View Count: ', item['statistics']['viewCount'])
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~')
         
         
# main function which acts as a controller
def run():
    while True:
        key = return_api()
        if type(key) == str:
            url = make_url(key)
            if type(url) == str:
                obj = make_request(url)
                if type(obj) == dict:
                    print_vid(obj)
                    break
                else:
                    continue
            else:
                continue
        

# imports all the libraries and runs the main function
if __name__ == '__main__':
    import json
    import urllib.request
    import urllib.parse
    run()
