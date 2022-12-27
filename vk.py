with open('vk_token.txt', 'r') as file:
    token = file.read().strip()
import requests


class VK:
    vk_url = 'https://api.vk.com/method/'
    def __init__(self, vk_token, version):
        self.params = {
            'access_token': vk_token,
            'v': version
        }

    def get_photos(self, owner_id):
        url = self.vk_url + 'photos.get'
        params = {
            'group_ids': id,
            'owner_id': owner_id,
            'album_id': 'profile',
            'extended': True,
            'count': 1
        }
        photos = requests.get(url, params={**self.params, **params}).json()
        photos_links_dict = []
        for photo in photos['response']['items']:
             for link in photo['sizes'][-1:]:
                photos_links_dict.append(link['url'])
        photos_links = ', '.join(photos_links_dict)
        return photos_links


    def get_name(self, owner_id):
        url = self.vk_url + 'photos.get'
        params = {
            'group_ids': id,
            'owner_id': owner_id,
            'album_id': 'profile',
            'extended': True,
            'count': 1
        }
        photos = requests.get(url, params={**self.params, **params}).json()
        file_name_dict = []
        for photo in photos['response']['items']:
            if str(photo['likes']['count']) + '.jpg' in file_name_dict:
                file_name_dict.append(str(photo['likes']['count']) + '_' + str(photo['date']) + '.jpg')
            else:
                file_name_dict.append(str(photo['likes']['count']) + '.jpg')
        file_name = ','.join(file_name_dict)
        return file_name


    def get_resault(self, owner_id):
        url = self.vk_url + 'photos.get'
        params = {
            'group_ids': id,
            'owner_id': owner_id,
            'album_id': 'profile',
            'extended': True,
            'count': 1

        }
        photos = requests.get(url, params={**self.params, **params}).json()
        res = []
        file_name = {}

        photos_size = {}
        for photo in photos['response']['items']:
            if str(photo['likes']['count']) + '.jpg' in file_name:
                file_name['name'] = str(photo['likes']['count']) + '_' + str(photo['date']) + '.jpg'
                res.append(file_name)
            else:
                file_name['name'] = str(photo['likes']['count']) + '.jpg'
                res.append(file_name)
            for link in photo['sizes'][-1:]:
                photos_size['size'] = link['type']
                res.append(photos_size)
        return res