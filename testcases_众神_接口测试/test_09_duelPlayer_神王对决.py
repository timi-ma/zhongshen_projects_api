import json

import requests
import config_全局配置文件.config_yaml

config = config_全局配置文件.config_yaml.zhongshen_yaml()

# 获取参数并使用
url_90 = config['config']['url_90']
port_90 = config['config']['port_90']
openid = config['config']['openid']
while_adventure = config['config']['while_adventure']
server_id = config['config']['server_id']


def test_Adventure_fighting():
    i = 1
    while i <= 100:
        base_url = f'{url_90}:{port_90}/mj-game-server/gods/game?n=json&m='
        params = {
            "open_id": f"{openid}",
            "csign": "8960ff1fb574addee72c2bf5dcbce3f3",
            "ctime": 1716878438996,
            "mid": "duel.duelPlayer",
            "duel_open_id": "WTQ5OUljQUNyaWUyakU5RDJSbE9Fdz09",
            "server_id": f"{server_id}"
        }
        params_json = json.dumps(params)
        api_url = f'{base_url}{params_json}'
        response = requests.post(api_url)
        assert response.status_code == 200
        print(response.text)
        print("神王对决接口请求成功")
        print("当前第" + f"{i}" + "次")
        i += 1
        pass
