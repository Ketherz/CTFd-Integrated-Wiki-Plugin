from flask import render_template


def load(app):
    @app.route('/wiki', methods=['GET'])
    def view_wiki():
        return render_template('page.html', content="<h1>Wiki</h1>")