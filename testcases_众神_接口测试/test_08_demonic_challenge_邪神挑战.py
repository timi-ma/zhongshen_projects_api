import json

import pytest
import requests
import config_全局配置文件.config_yaml

config = config_全局配置文件.config_yaml.zhongshen_yaml()

# 获取参数并使用
url_90 = config['config']['url_90']
openid = config['config']['openid']
while_adventure = config['config']['while_adventure']
server_id = config['config']['server_id']


@pytest.mark.parametrize("level_open, level_end", [(1, 70)])
def test_Adventure_fighting(level_open, level_end):
    for i in range(level_open, level_end):
        base_url = f'{url_90}/mj-game-server/gods/game?n=json&m='
        params = {
            "csign": "27e038f3cbff00a12dab96ccbde25e53",
            "ctime": 1716358924554,
            "mid": "gameCopy.challengeDemonKing",
            "level": f"{i}",
            "open_id": f"{openid}",
            "server_id": f"{server_id}"
        }
        params_json = json.dumps(params)
        api_url = f'{base_url}{params_json}'
        response = requests.post(api_url)
        data = json.loads(response.text)
        if data["ec"] == 200:
            print("邪神挑战成功")
            print("当前第" + f"{i}" + "层数")
            i += 1
        else:
            print(data["em"])
            break
