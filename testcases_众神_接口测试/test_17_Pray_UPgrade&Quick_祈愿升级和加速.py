import json

import pytest
import requests
import config_全局配置文件.config_yaml

config = config_全局配置文件.config_yaml.zhongshen_yaml()

# 获取参数并使用
url_90 = config['config']['url_90']
url_IDC = config['config']['url_IDC']
openid = config['config']['openid']
server_id = config['config']['server_id']


@pytest.mark.parametrize("star,end,step", [(5, 50, 1)])
def test_Pray_UPgrade_Quick(star, end, step):
    for i in range(star, end + 1, step):
        # 祈愿升级
        base_url_upgradePrayer = f'{url_90}/mj-game-server/gods/game?n=json&m='
        params_upgradePrayer = {
            "open_id": f"{openid}",
            "csign": "1c755740b4a5ab25c962674bbb886ea8",
            "ctime": 1716877006783,
            "mid": "pray.upgradePrayerSystem",
            "server_id": f"{server_id}"
        }
        params_json_upgradePrayer = json.dumps(params_upgradePrayer)
        api_url_upgradePrayer = f'{base_url_upgradePrayer}{params_json_upgradePrayer}'
        real_result_upgradePrayer = requests.post(api_url_upgradePrayer)
        print(api_url_upgradePrayer)
        print(real_result_upgradePrayer.text)

        # 祈愿快速升级
        base_url_quickenUpgrade = f'{url_90}/mj-game-server/gods/game?n=json&m='
        params_quickenUpgrade = {
            "open_id": f"{openid}",
            "csign": "0ebaa4e69676481c79e57d358fd09abe",
            "ctime": 1716877009368,
            "mid": "pray.quickenUpgrade",
            "num": 1100000,
            "server_id": f"{server_id}"
        }
        params_json_quickenUpgrade = json.dumps(params_quickenUpgrade)
        api_url_quickenUpgrade = f'{base_url_quickenUpgrade}{params_json_quickenUpgrade}'
        real_result_quickenUpgrade = requests.post(api_url_quickenUpgrade)
        print(api_url_quickenUpgrade)
        print(real_result_quickenUpgrade.text)
        data_upgradePrayer = json.loads(real_result_upgradePrayer.text)
        data_quickenUpgrade = json.loads(real_result_quickenUpgrade.text)
        if data_upgradePrayer["ec"] == 200 and data_quickenUpgrade["ec"] == 200:
            print("祈愿升级成功")
            print("当前第" + f"{i}" + "级")
            i += 1
        else:
            print(data_upgradePrayer["em"])
            print(data_quickenUpgrade["em"])
            break