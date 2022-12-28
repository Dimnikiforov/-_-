import requests
from vk import VK
with open('vk_token.txt', 'r') as file:
    vk_token = file.read().strip()
with open('ya_token.txt', 'r') as file:
    ya_token = file.read().strip()


class YaUploader:
    ya_url = 'https://cloud-api.yandex.net/'

    def __init__(self, ya_token):
        self.ya_token = ya_token

    def get_headers(self):
        return {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.ya_token}'}

    def create_folder(self):
        folder_name = str(input('input folder name:'))
        url = 'v1/disk/resources/'
        param = {'path': f'/{folder_name}', "overwrite": "false"}
        folder = requests.put(url=self.ya_url + url, headers=self.get_headers(), params=param)
        return folder_name

    def get_upload(self, vk_client=VK(vk_token, '5.131')):
        owner_id = str(input('input vk id:'))
        folder_name = self.create_folder()
        ph_names = vk_client.get_name(owner_id)
        ph_links = vk_client.get_photos(owner_id)
        url = 'v1/disk/resources/upload/'
        for name, link in zip(ph_names, ph_links):
            param_name = {'path': f'/{folder_name}/{name}'}
            param_link = {'url': link}
            res = requests.post(self.ya_url + url, headers=self.get_headers(), params={**param_link, **param_name})
        return vk_client.get_resault(owner_id)

