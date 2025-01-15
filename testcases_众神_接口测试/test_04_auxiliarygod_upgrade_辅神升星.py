import requests
import config_全局配置文件.config_yaml
import json
config = config_全局配置文件.config_yaml.zhongshen_yaml()

# 获取参数并使用
url_90 = config['config']['url_90']
port_90 = config['config']['port_90']
url_IDC = config['config']['url_IDC']
port_IDC = config['config']['port_IDC']
openid = config['config']['openid']
num = config['config']['num']
product_id = config['config']['product_id']
server_id = config['config']['server_id']


def test_send_gift():
    o = 1
    while o <= 130:
        i = 401
        while i <= 406:
            base_url = f"{url_90}:{port_90}/mj-game-server/gods/game?n=json&m="
            params = {
                "open_id": f"{openid}",
                "momo_token": "h5",
                "mid": "auxiliaryGod.upgradeLvlAuxiliaryGod",
                "server_id": f"{server_id}",
                "sn": f"{i}"
            }
            params_json = json.dumps(params)
            api_url = f'{base_url}{params_json}'

            response = requests.post(api_url)
            assert response.status_code == 200
            print('当前执行第' + str(i))
            print(response.text)
            i += 1
            pass
        o += 1
        print('\n当前执行第' + str(o))

    print("辅神升星完成")
