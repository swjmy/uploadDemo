from flask import render_template,url_for,request,flash
from . import main
from .. import db
from flask.ext.login import login_required,current_user
#真是醉了，现在secure_filename变更到.utils里
from werkzeug.utils import secure_filename
import os

@main.route('/')
def index():
    return render_template('index.html')

UPLOAD_FOLDER=os.path.abspath('./app/static/image')
ALLOWED_EXTENSIONS=set(['png','jpg','jpeg','gif'])

def allowed_file(filename):
    #从右往左切割一次，将分割的两个结果保存在一个list中
    #取得文件扩展名
    return '.'in filename and filename.rsplit('.',maxsplit=1)[1] in ALLOWED_EXTENSIONS


@login_required
@main.route('/upImage', methods=['POST','GET'])
def upImage():
    if request.method == 'POST':
        image = request.files['image']
        if image and allowed_file(image.filename):
            print('allowed_file')
            imagename = secure_filename(image.filename)
            if current_user.is_authenticated:
                imagefolder = os.path.join(UPLOAD_FOLDER,current_user.username)
                if not os.path.exists(imagefolder):
                    os.mkdir(imagefolder)  # 为该用户创建目录
                print(imagefolder)
                imagepath = os.path.join(imagefolder,imagename)
                image.save(imagepath)
                current_user.avatar_dir = imagepath
                db.session.add(current_user)
                db.session.commit()
            flash('上传成功')
            return render_template('upImage.html')
        else:
            print('not allowed file')
            flash('上传失败')
            return render_template('upImage.html')
    elif request.method == 'GET':
        return render_template('upImage.html')
