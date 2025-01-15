import json

import pytest
import requests
import config_全局配置文件.config_yaml

config = config_全局配置文件.config_yaml.zhongshen_yaml()

# 获取参数并使用
url_90 = config['config']['url_90']
url_IDC = config['config']['url_IDC']
openid = config['config']['openid']
while_adventure = config['config']['while_adventure']
server_id = config['config']['server_id']


@pytest.mark.parametrize("level_open, level_end", [(1, 200)])
def test_Adventure_fighting(level_open, level_end):
    for i in range(level_open, level_end):
        base_url = f'{url_90}/mj-game-server/gods/game?n=json&m='
        params = {
            "csign": "e5d89ea9bfc6d5515051c98f3d827a0c",
            "layer": f"{i}",
            "ctime": 1716886921694,
            "mid": "gameCopy.challengeHell",
            "open_id": f"{openid}",
            "server_id": f"{server_id}"
        }
        params_json = json.dumps(params)
        api_url = f'{base_url}{params_json}'
        print(api_url)
        response = requests.post(api_url)
        print(response.text)
        data = json.loads(response.text)
        if data["ec"] == 200 or data["em"] == "该层已挑战成功":
            print("当前第" + f"{i}" + "层数\n")
            i += 1
            print("炼狱挑战pass")
        else:
            print("=========================================")
            print("挑战失败，当前" + f"{i - 1}层，" + data["em"])
            break
