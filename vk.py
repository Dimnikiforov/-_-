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
            'count': 10
        }
        photos = requests.get(url, params={**self.params, **params}).json()
        photos_links_dict = []
        for photo in photos['response']['items']:
             for link in photo['sizes'][-1:]:
                photos_links_dict.append(link['url'])
        return photos_links_dict


    def get_name(self, owner_id):
        url = self.vk_url + 'photos.get'
        params = {
            'group_ids': id,
            'owner_id': owner_id,
            'album_id': 'profile',
            'extended': True,
            'count': 10
        }
        photos = requests.get(url, params={**self.params, **params}).json()
        file_name_dict = []
        for photo in photos['response']['items']:
            if str(photo['likes']['count']) + '.jpg' in file_name_dict:
                file_name_dict.append(str(photo['likes']['count']) + '_' + str(photo['date']) + '.jpg')
            else:
                file_name_dict.append(str(photo['likes']['count']) + '.jpg')
        return file_name_dict


    def get_resault(self, owner_id):
        url = self.vk_url + 'photos.get'
        params = {
            'group_ids': id,
            'owner_id': owner_id,
            'album_id': 'profile',
            'extended': True,
            'count': 10

        }
        photos = requests.get(url, params={**self.params, **params}).json()
        res = []
        file_name = {}
        photos_dict = self.get_name(owner_id)
        photos_size = {}
        for ph in photos_dict:
            file_name['name'] = ph
        for photo in photos['response']['items']:
            for link in photo['sizes'][-1:]:
                photos_size['size'] = link['type']
            res.append(file_name)
            res.append(photos_size)
        return res