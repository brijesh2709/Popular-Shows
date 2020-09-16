# Constructivist style

# Sample code from github
'''
#!/usr/bin/env python
import sys, re, operator, string, inspect

#
# The functions
#
def extract_words(path_to_file):
    if type(path_to_file) is not str or not path_to_file:
        return []

    try:
        with open(path_to_file) as f:
            str_data = f.read()
    except IOError as e:
        print("I/O error({0}) when opening {1}: {2}".format(e.errno, 
               path_to_file, e.strerror))
        return []
    
    pattern = re.compile('[\W_]+')
    word_list = pattern.sub(' ', str_data).lower().split()
    return word_list

def remove_stop_words(word_list):
    if type(word_list) is not list:
        return [] 

    try:
        with open('../stop_words.txt') as f:
            stop_words = f.read().split(',')
    except IOError as e:
        print("I/O error({0}) when opening ../
                stops_words.txt: {1}".format(e.errno, e.strerror))
        return word_list

    stop_words.extend(list(string.ascii_lowercase))
    return [w for w in word_list if not w in stop_words]

def frequencies(word_list):
    if type(word_list) is not list or word_list == []:
        return {}

    word_freqs = {}
    for w in word_list:
        if w in word_freqs:
            word_freqs[w] += 1
        else:
            word_freqs[w] = 1
    return word_freqs

def sort(word_freq):
    if type(word_freq) is not dict or word_freq == {}:
        return []

    return sorted(word_freq.items(), key=operator.itemgetter(1), reverse=True)

#
# The main function
#
filename = sys.argv[1] if len(sys.argv) > 1 else "../input.txt"
word_freqs = sort(frequencies(remove_stop_words(extract_words(filename))))

for tf in word_freqs[0:25]:
    print(tf[0], ' - ', tf[1])
'''

# Explanation
'''
    The above mentioned code is the contructivist style code by Dr. Crista
Lopez. According to the description, every single function checks the sanity
of its arguments returns something sensible or assigns them reasonable values.
All code blocks check for possible errors and escape the block when things go
wrong. Error handling is taken into detailed consideration. In my code I had
followed the same structure as Lopez's style. I had also handled errors in the
desired way. Every function in my code serves its ows purpose and returns
something sensible and passes on the traits to each function.
'''

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
