from datetime import datetime
from flask import render_template, session, redirect, url_for, jsonify
from . import main
from .forms import *
from ..models import *

@main.route('/', methods=['GET', 'POST'])
def index():
	#form = NameForm()
	#f form.validate_on_submit():
	#	return redirect(url_for('.index'))

	return render_template('index.html')

@main.route('/campaign', methods=['GET'])
def get_all_campaign():
	campaign = Campaign.query.all()
	return jsonify({'campaign': campaign})

