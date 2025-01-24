import requests
import pytest
import config_全局配置文件.config_yaml
config = config_全局配置文件.config_yaml.zhongshen_yaml()

# 获取参数并使用
url_90 = config['config']['url_90']
url_IDC = config['config']['url_IDC']
openid = config['config']['openid']
num = config['config']['num']
product_id = config['config']['product_id']
server_id = config['config']['server_id']


@pytest.mark.parametrize("star,end,step", [(99001, 99006, 1)])
def test_send_gift(star, end, step):
    for i in range(star, end + 1, step):
        api_url = f"{url_90}/debug/addProduct?open_id={openid}&product_id={i}&num={num}&server_id={server_id}"
        # api_url = f"{url_IDC}/debug/addProduct?open_id={openid}&product_id={i}&num={num}&server_id={server_id}"
        # 执行相关操作
        response = requests.post(api_url)
        assert response.status_code == 200
        print('当前执行第' + str(i))
        print(api_url)
        print(response.text)
    print("发礼物成功")