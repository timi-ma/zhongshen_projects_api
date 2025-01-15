import yaml


def zhongshen_yaml():
    with open('E:/develop/pycharm/接口自动化/resources_接口数据文件/zhongshen_config.yaml', 'r') as file:
        config = yaml.safe_load(file)
        return config
