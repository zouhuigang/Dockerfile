#!/usr/bin/python3
import bottle
import base64
import json
import time
import random
from MyQR import myqr
import os
#
def corsHandle(function):
    def temp(*args,**kwargs):
        bottle.response.headers['Access-Control-Allow-Origin']='*'
        bottle.response.headers['Access-Control-Allow-Methods']='GET,POST,PUT,OPTIONS'
        bottle.response.headers['Access-Control-Allow-Headers']='Origin,Accept,Content-Type,X-Requested-With,X-CSRF-Token'
        if bottle.request.method!='OPTIONS':
            return function(*args,**kwargs)
    return temp
#
def filePutContents(file,content):
    fp=open(file,'wb')
    fp.write(content)
    fp.close()
def getDateTime(offset_day=0):
    timestamp=time.time()
    if offset_day!=0:
        timestamp+=offset_day*86400
    DATE_TIME=time.localtime(timestamp)
    return time.strftime('%Y%m%d-%H%M%S',DATE_TIME)
#
@bottle.route('/temp/<name>')
def staticFile(name):
    return bottle.static_file(name,root='/app/temp')
#
@bottle.post('/color/qrcode')
@corsHandle
def colorQrcode():
    wordsPost=bottle.request.forms.get('words')
    versionPost=int(bottle.request.forms.get('version'))
    levelPost=bottle.request.forms.get('level')
    colorizedPost=bottle.request.forms.get('colorized')
    contrastPost=float(bottle.request.forms.get('contrast'))
    brightnessPost=float(bottle.request.forms.get('brightness'))
    picturePost=bottle.request.forms.get('picture')
    if colorizedPost=='1':
        colorizedPost=True
    else:
        colorizedPost=False
    pictureType='jpg'
    if picturePost!='':
        temp=picturePost.split(',')
        if temp[0]=='data:image/png;base64':
            pictureType='png'
        elif temp[0]=='data:image/gif;base64':
            pictureType='gif'
        elif temp[0]=='data:image/jpeg;base64':
            pictureType='jpg'
        pictureData=base64.b64decode(temp[1])
        fileName='/app/temp/upload-%s-%s.%s' % (getDateTime(),random.randint(1000,9999),pictureType)
        filePutContents(fileName,pictureData)
    else:
        fileName=None
    fileSaveName='%s-%s.%s' % (getDateTime(),random.randint(1000,9999),pictureType)
    myqr.run(
        wordsPost,
        versionPost,
        levelPost,
        fileName,
        colorizedPost,
        contrastPost,
        brightnessPost,
        fileSaveName,
        'temp'
    )
    result={}
    result['status']='0'
    result['msg']=''
    result['data']={}
    result['data']['src']='%s/temp/%s' % (os.getenv('DOCKER_COLOR_QRCODE_URL'),fileSaveName)
    content=json.dumps(result)
    return content
#
bottle.run(host='0.0.0.0',port=50001,debug=True)
