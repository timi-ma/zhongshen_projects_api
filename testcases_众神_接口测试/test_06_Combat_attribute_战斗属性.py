import requests
import config_全局配置文件.config_yaml

config = config_全局配置文件.config_yaml.zhongshen_yaml()

# 获取参数并使用
url_90 = config['config']['url_90']
port_90 = config['config']['port_90']
url_IDC = config['config']['url_IDC']
port_IDC = config['config']['port_IDC']
openid = config['config']['openid']
challenger = config['config']['challenger']
server_id = config['config']['server_id']


def test_Combat_attribute():
    api_url = f"{url_90}:{port_90}/debug/testFightPlayer?open_id={openid}&challenger={challenger}&server_id={server_id}"
    # api_url = f"{url_IDC}:{port_IDC}/debug/testFightPlayer?open_id={openid}&challenger={challenger}&server_id={server_id}"
    response = requests.post(api_url)
    assert response.status_code == 200
    print(response.text)
    print("查战斗属性成功")
