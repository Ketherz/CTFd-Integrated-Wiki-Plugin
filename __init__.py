from flask import render_template, Blueprint
from CTFd.plugins import register_plugin_assets_directory
import os

# TODO: It will be better to use the database to store everyfiles, but we will see that later
""" This function is used to display all the files containing soluces the solutions are in the folder soluce """

def define_wiki(app) :
    wiki_blueprint = Blueprint('wiki', __name__, template_folder='templates', static_folder='assets')
    @wiki_blueprint.route("/wiki", methods=["GET"])
    def wiki():
        soluce_file = []
        directory = os.path.dirname(os.path.realpath(__file__)) + "/soluce"
        for filename in os.listdir(directory) :
            soluce_file.append(filename)

        return render_template('wiki.html', soluce_file = soluce_file, title = "Wiki")
    app.register_blueprint(wiki_blueprint)


def load(app):
    define_wiki(app)
