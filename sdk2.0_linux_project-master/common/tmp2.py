import yaml


def get_config_data():
    # 获取配置文件数据
    # logging.info('get_config_data')
    with open('./config/config.yaml', 'r') as file:
        data = yaml.load(file)

    return data

def gen_app():
    data = get_config_data()['base_dir']
    for app in data:
        listapp = []
        listapp.append(app)
    return listapp

if __name__ == '__main__':
    get_config_data()
    alist = gen_app()
    for app in alist:
        print(app)