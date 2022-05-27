import json
import time
import os


def order_files(data):
    types_dictionary = {}
    for file_type in data['types']:
        if not os.path.exists(file_type['path']):
            os.makedirs(file_type['path'])
        types_dictionary[file_type['type']] = file_type['path']

    for file in os.listdir(data['downloads_folder']):
        file_name, file_type = os.path.splitext(file)

        if file_type and file_type in types_dictionary:
            os.rename(data['downloads_folder'] + '/' + file, types_dictionary[file_type] + '/' + file)


if __name__ == '__main__':
    with open('config.json', 'r') as json_file:
        config = json.load(json_file)
    loop_time = config['loop_every_x_second']
    while True:
        order_files(config)
        time.sleep(loop_time)
