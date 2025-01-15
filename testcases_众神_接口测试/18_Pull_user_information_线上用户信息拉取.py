import json

import requests

pull_openid = 'MEV3SmdLTHN4V0M0b1QxTE9NYWdIQT09'
server_id = '10002'


# def pull_user_info():
pull_url = f'https://mmmj.immomogame.com/mj-game-server/gods/backup_user_info?open_id={pull_openid}&save_mysql=0&server_id={server_id}'
print(pull_url)
response = requests.post(pull_url)
assert response.status_code == 200
pull_user_info_json = response.json()
pull_user = pull_user_info_json.get('data', {}).get('info')
print(pull_user)

#
# if __name__ == "__main__":
#     pull_user_info()
