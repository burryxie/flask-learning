from flask import Flask,render_template,request,flash,redirect,url_for
from database.data import load_recent_3jobs_from_db,load_all_jobs_from_db,load_job_detail_from_db,add_application_to_db
from database.notification import send_notification
import os
import datetime
from werkzeug.utils import secure_filename


UPLOAD_FOLDER = './upload_files/'
ALLOWED_EXTENSIONS = { 'pdf', 'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 10 * 1000 * 1000 #上传文件最大10MB



@app.route("/")
def home():
    # return "Hello, Flask!"
    jobs = load_recent_3jobs_from_db()
    return render_template('index.html',jobs=jobs)
3
@app.route("/news")
def news_info():
    return render_template('news.html')

@app.route("/news/news_detail")
def news_detail_info():
    return render_template('news_detail.html')

@app.route("/bussiness_info")
def business_info():
    return render_template('bussiness_info.html')

@app.route("/job_listing")
def job_listing():
    jobs = load_all_jobs_from_db()
    return render_template('job_listing.html',jobs=jobs,num_jobs=len(jobs))

@app.route("/job_detail/<id>")
def job_detail(id):
    job_detail = load_job_detail_from_db(id)
    return render_template('job_detail.html',job=job_detail[0])


@app.route("/job_apply/<id>")
def job_apply(id):
    job_detail = load_job_detail_from_db(id)
    return render_template('job_apply.html',job=job_detail[0])


def get_current_date():
    # 获取当前日期
    current_date = datetime.date.today()
    # 将日期转换为字符串格式
    current_date_string = current_date.strftime("%Y-%m-%d")
    # 打印结果
    return current_date_string

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/job_apply_submit",methods=['post'])
def job_apply_submit():
    # if request.method == 'POST':
    #     # check if the post request has the file part
    #     if 'file' not in request.files:
    #         flash('No file part')
    #         return redirect(request.url)
    #     file = request.files['resume_file']
    #     # If the user does not select a file, the browser submits an
    #     # empty file without a filename.
    #     if file.filename == '':
    #         flash('No selected file')
    #         return redirect(request.url)
    #     if file and allowed_file(file.filename):
    #         filename = secure_filename(file.filename)
    #         file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    #         # return redirect(url_for('download_file', name=filename))
    # return ''

    data = request.form.to_dict()
    data['resume_file']= request.files['resume_file'].filename
    resume_file = request.files['resume_file']
    resume_filename = resume_file.filename 
    target_file_path = os.path.join(app.config['UPLOAD_FOLDER'],get_current_date(),data['job_title'])
    if not os.path.exists(target_file_path):
        os.makedirs(target_file_path)
                          
    resume_file.save(os.path.join(app.config['UPLOAD_FOLDER'],get_current_date(),data['job_title'], '['+get_current_date()+']'+data['name']+'_'+data['job_title']+'_'+resume_filename))
    add_application_to_db(data)
    jobs = load_recent_3jobs_from_db()
    send_notification(target_file_path,'['+get_current_date()+']'+data['name']+'_'+data['job_title']+'_'+resume_filename)

    return render_template('index.html',jobs=jobs)


