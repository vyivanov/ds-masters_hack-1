import os
import sys
import json

path = sys.argv[1]

cfg = json.load(open(path, 'r'))
t = open(cfg['output']['spec_file'], 'r')
spc = json.load(t)
t.close()

data_path = cfg['input']['data_path']
logs_path = cfg['input']['logs_path']

logs = []
for file in os.listdir(logs_path):
    logs = logs + json.load(open(logs_path + file, 'r'))

pathes = (
    data_path + 'kids/NG/',
    data_path + 'kids/OK/',
    data_path + 'men/NG/',
    data_path + 'men/OK/',
    data_path + 'women/NG/',
    data_path + 'women/OK/',
)

cnt = 0
for path in pathes:
    idx = 0
    for pic in os.listdir(path):
        for log in logs:
            if log['image_filename'] == pic:
                name = '{}.{}'.format('%04d' % idx, pic.split('.')[-1])
                os.rename(path + pic, path + name)
                spc['images'].append({
                    ' ## ': cnt,
                    'path': os.path.relpath(path, start='../..') + '/' + name,
                    'link': log['image_link']})
                cnt = cnt + 1
                idx = idx + 1
                break
        else:
            if pic != '.DS_Store':
                os.remove(path + pic)

t = open(cfg['output']['spec_file'], 'w')
json.dump(spc, t, indent=4)
