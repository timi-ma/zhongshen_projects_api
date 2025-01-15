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


@pytest.mark.parametrize("level_open, level_end", [(1, 550)])
def test_Adventure_fighting(level_open, level_end):
    base_url = f'{url_90}/mj-game-server/gods/game?n=json&m='
    # base_url = f'{url_IDC}/mj-game-server/gods/game?n=json&m='
    params = {
        "open_id": f"{openid}",
        "momo_token": "h5",
        "mid": "mainLine.battle",
        "server_id": f"{server_id}"
    }
    for i in range(level_open, level_end):
        params_json = json.dumps(params)
        api_url = f'{base_url}{params_json}'
        response = requests.post(api_url)
        data = json.loads(response.text)
        if data["ec"] == 200:
            print("冒险挑战成功")
            print("当前第" + f"{i}" + "关")
            i += 1
        else:
            print(data["em"])
            break


import requests


def test_api():
    # 接口的 URL
    api_url = "http://example.com/api"
    # 发送请求，这里以 GET 请求为例，你可以根据实际情况修改为 POST、PUT 等请求方法
    response = requests.get(api_url)

    # 检查响应状态码是否为 200
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

    # 提取响应内容
    response_content = response.text
    print(f"Response content: {response_content}")

    # 提取响应的 JSON 数据（如果响应是 JSON 格式）
    try:
        response_json = response.json()
        print(f"Response JSON data: {response_json}")
        # 假设你想提取 JSON 中的某个键值对，例如 'key' 的值
        value_of_key = response_json.get('key')
        print(f"Value of 'key': {value_of_key}")
    except ValueError:
        print("Response is not in JSON format")

    # 提取响应的 headers
    response_headers = response.headers
    print(f"Response headers: {response_headers}")
    # 假设你想提取 headers 中的某个键值对，例如 'Content-Type' 的值
    content_type = response_headers.get('Content-Type')
    print(f"Content-Type: {content_type}")


if __name__ == "__main__":
    test_api()









