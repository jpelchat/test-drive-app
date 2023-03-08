# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from apps.home import blueprint
from flask import render_template, request
from flask_login import login_required
from jinja2 import TemplateNotFound
import sys
import os

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@blueprint.route('/index')
def index():
    return render_template('pages/index.html', segment='index')

@blueprint.route('/fakeindex')
def fakeindex():
    return render_template('pages/fakeindex.html', segment='index')

@blueprint.route('/success', methods=['GET'])
def success():
     return render_template('pages/success.html', segment='index')

@blueprint.route('/result', methods=['GET'])
def result():
    if not os.path.exists('success.file'):
        os.mknod('success.file')
    return render_template('pages/success.html', segment='index')

@blueprint.route('/typography')
def typography():
    return render_template('pages/typography.html')

@blueprint.route('/color')
def color():
    return render_template('pages/color.html')

@blueprint.route('/icon-tabler')
def icon_tabler():
    return render_template('pages/icon-tabler.html')

@blueprint.route('/sample-page')
def sample_page():
    return render_template('pages/sample-page.html')  

@blueprint.route('/accounts/password-reset/')
def password_reset():
    return render_template('accounts/password_reset.html')

@blueprint.route('/accounts/password-reset-done/')
def password_reset_done():
    return render_template('accounts/password_reset_done.html')

@blueprint.route('/accounts/password-reset-confirm/')
def password_reset_confirm():
    return render_template('accounts/password_reset_confirm.html')

@blueprint.route('/accounts/password-reset-complete/')
def password_reset_complete():
    return render_template('accounts/password_reset_complete.html')

@blueprint.route('/accounts/password-change/')
def password_change():
    return render_template('accounts/password_change.html')

@blueprint.route('/accounts/password-change-done/')
def password_change_done():
    return render_template('accounts/password_change_done.html')

@blueprint.route('/<template>')
def route_template(template):

    try:

        if not template.endswith('.html'):
            template += '.html'

        # Detect the current page
        segment = get_segment(request)

        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template("home/" + template, segment=segment)

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except:
        return render_template('home/page-500.html'), 500

# Helper - Extract current page name from request
def get_segment(request):

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None
