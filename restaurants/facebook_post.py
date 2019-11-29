import sys
import os
import json
import requests
import datetime
import filecmp


class Facebook:
    @staticmethod
    def get_access_token(token_name):
        access_token = os.getenv('PWD') + '/access_tokens.sh'
        f = open(access_token, 'r+')
        lines = f.readlines()
        for line in lines:
            tokens = line.strip().split('=')
            if tokens[0] == token_name:
                return tokens[1].strip()

        return 'Not found'

    def __init__(self):
        self.page_id = Facebook.get_access_token('FACEBOOK_PAGE_ID')
        self.page_access_token = Facebook.get_access_token('FACEBOOK_PAGE_ACCESS_TOKEN')



    def publish_photo_msg(self, message, image_url):


if __name__ == '__main__':
    facebook = Facebook()

    message = my_name + ' likes this ice-cream!'
    facebook.publish_photo_msg(message, image_url)
