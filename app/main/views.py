from . import main
from flask import render_template, request, url_for, make_response, flash, redirect, current_app
from .form import PostForm,DeleteForm
import os
from manager import app
import datetime
import random
from ..model import Article
from .. import db
from flask_login import login_required

def gen_rnd_filename():
    filename_prefix = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    return '%s%s' % (filename_prefix, str(random.randrange(1000, 10000)))

@main.route('/')
def index():
    return render_template("index.html")

@main.route('/blog')
def blog():
    #分页
    page = request.args.get('page',1,type=int)
    pagination = Article.query.order_by(Article.id.desc()).paginate(page,
                                                                  per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
                                                                  error_out=False)
    articles = pagination.items

    for article in articles:
        postition = article.article.find("</p>")
        article.article = article.article[:postition]
    return render_template("blog.html",articles=articles, pagination=pagination)


@main.route('/post', methods=['GET', 'POST'])
@login_required
def post():
    form = PostForm()
    if form.validate_on_submit():
        article = Article(article=form.body.data)
        db.session.add(article)
        db.session.commit()
        flash("提交文章成功！")
        return redirect(url_for("main.post"))
    return render_template("post.html", form=form)

@main.route('/delete', methods=['GET', 'POST'])
@login_required
def delete():
    form = DeleteForm()
    if form.validate_on_submit():
        article = Article.query.get_or_404(form.id.data)
        db.session.delete(article)
        db.session.commit()
        flash("成功删除文章")
    return render_template("delete.html",form=form)

@main.route('/me')
def me():
    return render_template("me.html")


@main.route('/article/<int:id>')
def article(id):
    article = Article.query.get_or_404(id)
    return render_template('article.html', article=article)

@main.route('/ckupload/', methods=['POST', 'OPTIONS'])
def ckupload():
    """CKEditor file upload"""
    error = ''
    url = ''
    callback = request.args.get("CKEditorFuncNum")

    if request.method == 'POST' and 'upload' in request.files:
        fileobj = request.files['upload']
        fname, fext = os.path.splitext(fileobj.filename)
        rnd_name = '%s%s' % (gen_rnd_filename(), fext)

        filepath = os.path.join(app.static_folder, 'upload', rnd_name)

        # 检查路径是否存在，不存在则创建
        dirname = os.path.dirname(filepath)
        if not os.path.exists(dirname):
            try:
                os.makedirs(dirname)
            except:
                error = 'ERROR_CREATE_DIR'
        elif not os.access(dirname, os.W_OK):
            error = 'ERROR_DIR_NOT_WRITEABLE'

        if not error:
            fileobj.save(filepath)
            url = url_for('static', filename='%s/%s' % ('upload', rnd_name))
    else:
        error = 'post error'

    res = """<script type="text/javascript">
  window.parent.CKEDITOR.tools.callFunction(%s, '%s', '%s');
</script>""" % (callback, url, error)

    response = make_response(res)
    response.headers["Content-Type"] = "text/html"
    return response

