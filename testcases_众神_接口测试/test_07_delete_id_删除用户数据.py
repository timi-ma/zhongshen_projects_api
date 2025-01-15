import requests
import config_全局配置文件.config_yaml

config = config_全局配置文件.config_yaml.zhongshen_yaml()

# 获取参数并使用
url_90 = config['config']['url_90']
url_IDC = config['config']['url_IDC']
openid = config['config']['openid']
server_id = config['config']['server_id']


def test_delete_id():
    api_url = f"{url_90}/debug/delUser?open_id={openid}&server_id={server_id}"
    # api_url = f"{url_IDC}/debug/delUser?open_id={openid}&server_id={server_id}"
    print(api_url)
    response = requests.post(api_url)

    assert response.status_code == 200

    print("清号成功")
