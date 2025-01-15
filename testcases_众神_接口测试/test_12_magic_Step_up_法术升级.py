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


def test_send_gift():
    o = 1
    while o <= 51:
        i = 101
        while i <= 113:
            base_url = f"{url_90}/mj-game-server/gods/game?n=json&m="
            params = {
                    "open_id": f"{openid}",
                    "csign": "85e5ee1db40701ed55e0cf9b3127a950",
                    "ctime": 1716800761414,
                    "mid": "magicArts.upgradeStageMagicArts",
                    "sn": f"{i}",
                    "server_id": f"{server_id}"
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
        print('------------------------------')
        print('\n当前执行第' + str(o))

    print("法术升级完成")
