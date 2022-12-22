from vk import VK
from ya import YaUploader
with open('vk_token.txt', 'r') as file:
    vk_token = file.read().strip()
with open('ya_token.txt', 'r') as f:
    ya_token = f.read().strip()
if __name__ == '__main__':
    vk_client = VK(vk_token, '5.131')
    ya_disk = YaUploader(ya_token)
    print(ya_disk.get_upload())


