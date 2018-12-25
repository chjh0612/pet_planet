# encoding: utf-8
#@author: chenjunhua
#time: 2018/12/25 17:23

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = '8000', debug = True)