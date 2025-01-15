import requests
import config_全局配置文件.config_yaml
import json
config = config_全局配置文件.config_yaml.zhongshen_yaml()

# 获取参数并使用
url_90 = config['config']['url_90']
url_IDC = config['config']['url_IDC']
openid = config['config']['openid']
num = config['config']['num']
product_id = config['config']['product_id']
server_id = config['config']['server_id']


def test_magic_Activate():
    i = 201
    while i <= 213:
        base_url = f"{url_IDC}/mj-game-server/gods/game?n=json&m="
        params = {
                "open_id": f"{openid}",
                "csign": "71452e5a391d3539cdbfb50b816fe109",
                "ctime": 1716811916876,
                "mid": "magicArts.activateMagicArts",
                "sn": f"{i}",
                "server_id": f"{server_id}"
            }
        params_json = json.dumps(params)
        api_url = f'{base_url}{params_json}'

        response = requests.post(api_url)
        print(api_url)
        assert response.status_code == 200
        print('当前执行第' + str(i))
        print(response.text)
        i += 1
        pass

    print("法术激活完成")
