# Launch with
#
# gunicorn -D --threads 4 -b 0.0.0.0:5000 --access-logfile server.log --timeout 60 server:app glove.6B.300d.txt bbc

# gunicorn -D --threads 1 -b 0.0.0.0:5000 --access-logfile server.log --timeout 60 server:app /Users/kirsten/Documents/USF/2019Fall/DataAcquisition/SelfRepo/recommendation/recommender-Kirsten-Tsai/Data/glove.6B/glove.6B.50d.txt /Users/kirsten/Documents/USF/2019Fall/DataAcquisition/SelfRepo/recommendation/recommender-Kirsten-Tsai/Data/bbcTest

from flask import Flask, render_template
from doc2vec import *
import sys

app = Flask(__name__)

@app.route("/")
def articles():
    """Show a list of article titles"""
    titles = [ _[1] for _ in articles]
    links = [ "/article/" + _[0] for _ in articles]
    return render_template('articles.html', all = zip(titles, links))

@app.route("/article/<topic>/<filename>")
def article(topic,filename):

    """
    Show an article with relative path filename. Assumes the BBC structure of
    topic/filename.txt so our URLs follow that.
    """
    with open(articles_dirname+"/"+topic+"/"+filename, "r") as f:
        txt = f.read()
        txt = txt.split("\n")
    seealso = recommended(topic+"/"+filename, articles, 5)
    moreArticle = [_[1] for _ in seealso]
    moreLink = ["/article/" + _[0] for _ in seealso]
    return render_template('article.html',topic = txt[0], content = txt[1:], all = zip(moreArticle, moreLink))
# initialization
i = sys.argv.index('server:app')

vectorfile = "/Users/kirsten/Documents/USF/2019Fall/DataAcquisition/SelfRepo/recommendation/recommender-Kirsten-Tsai/glove.6B.300d.txt"
bbcpath = "/Users/kirsten/Documents/USF/2019Fall/DataAcquisition/SelfRepo/recommendation/recommender-Kirsten-Tsai/bbc"


try:
    glove_filename = sys.argv[i+1]
    articles_dirname = sys.argv[i+2]
except:
    glove_filename = vectorfile
    articles_dirname = bbcpath

gloves = load_glove(glove_filename)
articles = load_articles(articles_dirname, gloves)
