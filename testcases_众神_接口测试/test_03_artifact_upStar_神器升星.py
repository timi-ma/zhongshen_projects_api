import json

import requests
import config_全局配置文件.config_yaml

config = config_全局配置文件.config_yaml.zhongshen_yaml()

# 获取参数并使用
url_90 = config['config']['url_90']
url_IDC = config['config']['url_IDC']
openid = config['config']['openid']
while_artifact_upStar = config['config']['while_artifact_upStar']
server_id = config['config']['server_id']


def test_artifact_upStar():
    o = 1
    while o <= while_artifact_upStar:
        i = 16
        while i <= 16:
            base_url = f'{url_90}/mj-game-server/gods/game?n=json&m='
            params = {
                "open_id": f"{openid}",
                "momo_token": "h5",
                "csign": "f1c0e78ff9020c939cd8b343be719395",
                "ctime": 1720007872349,
                "server_id": f"{server_id}",
                "sn": f"{i}",
                "mid": "artifact.upStar"
            }
            params_json = json.dumps(params)
            api_url = f'{base_url}{params_json}'
            real_result = requests.post(api_url)
            print(api_url)
            print(real_result.text)
            i += 1
            pass
        o += 1
        pass
    print("神器升星成功")


