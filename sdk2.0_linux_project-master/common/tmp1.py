import os
import subprocess
import pyscreenshot
import time
import psutil
import yaml
import re

# a = time.strftime('%Y-%m-%d-%H-%M-%S')
# print(a)
# im = pyscreenshot.grab()
# os.system('mkdir /home/root/screenshot')
# im.save('abc.png')

# os.mkdir('./screenshot')
# command = 'gnome-screenshot -f' +\
#           ' ./screenshot/' + \
#           time.strftime('%Y-%m-%d-%H-%M-%S') + '.png'
# os.system(command)

#
# list = psutil.pids()
# for wnd in list:
#     p = psutil.Process(wnd)
#     pname = p.name()
#     print(wnd, pname)
#     # p.terminal()


dir = r'/root/Programe/AstraSDK-v2.0.13-5a10c0cc62-20181122T123809Z-Linux/bin'
# shit_list = []
applist = os.listdir(dir)

def kill_app(p):
    comm = 'kill -9 '+ str(p)
    # os.system('TASKKILL /PID %s /T /F' % p.pid)
    os.system(comm)
def gen_app():
    shit_list = []
    for app in applist:
        if app.find('.') == -1:
            # print(app)
            shit_list.append(app)
    return shit_list

def start_app(app):
    com = "./" + app
    shit = subprocess.Popen(com,stdout=subprocess.PIPE,shell=True)
    # print(shit.pid)
    time.sleep(5)
    dd = shit.pid
    kill_app(dd + 1)



# alist = gen_app()
os.chdir(dir)
for app in enumerate(gen_app(), 1):
    print(app)


# print(shit_list)
# print(gen_app().__next__())
# os.chdir(dir)
# # os.system('cd /root/Programe/AstraSDK-v2.0.13-5a10c0cc62-20181122T123809Z-Linux/bin')
# comm = './SimpleColorViewer-SFML'
#
# aaaa = subprocess.Popen(comm, stdout=subprocess.PIPE, shell=True)
# print(aaaa.pid)
# out = aaaa.communicate()
# aaaa.pid

