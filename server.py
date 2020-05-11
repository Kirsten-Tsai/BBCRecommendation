# Launch with
#
# gunicorn -D --threads 4 -b 0.0.0.0:5000 --access-logfile server.log --timeout 60 server:app glove.6B.300d.txt bbc

from flask import Flask, render_template
from doc2vec import *
import sys
import os

app = Flask(__name__)

@app.route("/")
def articles():
    """Show a list of article titles"""
    
    return render_template('articles.html', ls_articles=ls_articles)


@app.route("/article/<topic>/<filename>")
def article(topic,filename):
    """
    Show an article with relative path filename. Assumes the BBC structure of
    topic/filename.txt so our URLs follow that.
    """
    
    for a in ls_articles:
    	if a[0]==os.path.join(topic,filename):
    		show_article = a.copy()

    show_article[2] = show_article[2].split('<p>')
    seealso = recommended(show_article, ls_articles, 5)
    return render_template('article.html', article=show_article, ls_seealso=seealso)

# initialization
i = sys.argv.index('server:app')
glove_filename = sys.argv[i+1]
articles_dirname = sys.argv[i+2]

gloves = load_glove(glove_filename)
ls_articles = load_articles(articles_dirname, gloves)
