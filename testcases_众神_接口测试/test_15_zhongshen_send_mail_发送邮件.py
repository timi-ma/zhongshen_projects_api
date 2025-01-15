import requests
import config_全局配置文件.config_yaml

config = config_全局配置文件.config_yaml.zhongshen_yaml()

# 获取参数并使用
url_90 = 'http://47.95.240.88:9621/mj-game-server/inner/gods/gods_official_email_one'
url_IDC = config['config']['url_IDC']
openid = config['config']['openid']
momoids = config['config']['momoids']
server_id = config['config']['server_id']


def test_zhongshen_Personal_mail():
    i = 1
    while i <= 90:
        api_url = f"{url_90}?server_id={server_id}&momo_ids={momoids}&title=女神节感恩回馈&content=女神节感恩回馈女神节感恩回馈&reward=100008:1"
        # api_url = f"{url_IDC}/debug/delUser?open_id={openid}&server_id={server_id}"
        print(api_url)
        response = requests.post(api_url)
        assert response.status_code == 200
        print("发送邮件成功")
        i += 1
