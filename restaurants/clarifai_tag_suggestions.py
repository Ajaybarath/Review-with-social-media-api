import json
import requests


def get_tags_suggestions(api_key, image_url):

def get_access_token(token_name):
    f = open('access_tokens.sh', 'r+')
    lines = f.readlines()
    f.close()
    for line in lines:
        tokens = line.strip().split('=')
        if tokens[0] == token_name:
            return tokens[1].strip()
    return 'Not found'

if __name__ == '__main__':
    api_key = get_access_token('CLARIFAI_API_KEY')
    image_url = 'https://i.imgur.com/dlMjqQe.jpg'
    tags_suggessted = get_tags_suggestions(api_key, image_url)
    print(tags_suggessted)
