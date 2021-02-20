import flask
from flask import Flask, render_template
from flask.logging import create_logger
from flask.logging import logging

APP = Flask(__name__)

##An error is getting thrown that states "Method 'logger' has not 'info' member"
##Our friendly neighborhood google is only aiding me as if its the LOG for bugs and not routing.
##My suspicions for why it won't run is ALL HERE in the app.py file, and I can't figure it out.

##UPDATE 12/13/2020 --> Note for Professor
##My code was throwing a false positive that logger was missing the variable .info
##I had to go into the settings.JSON file and add code to add info as a member despite it already being there.
##I added this line of code below and it worked for me. 
##"python.linting.pylintArgs": ["--generate-members"]

@APP.route('/')
def index():
    APP.logger.info("Switching to the Index Page")
    return render_template('index.html')

@APP.route('/home')
def home():
    APP.logger.info("Switching to the Home Page")
    return render_template('home.html')

@APP.route('/about')
def about():
    APP.logger.info("Switching to the About Page")
    return render_template('about.html')

##I added a new route for Podcasts, given that that is my whole personlity aside from computers
##This could also be the issue but I made it exactly the same way as the others, so I doubt it.
@APP.route('/podcasts')
def personality():
    APP.logger.info("Switching to the Podcasts Page")
    return render_template('podcasts.html')

@APP.route('/contact')
def contact():
    APP.logger.info("Switching to the Contact Me Page")
    return render_template('contact.html')

@APP.route('/404')
def four_oh_four():
    APP.logger.info("Switching to the 404 Page, This is a test page so we don't need to error here.")
    return render_template('four_oh_four.html')

@APP.errorhandler(404)
def page_not_found(error):
    APP.logger.warning("Switching to the 404 Page")
    return render_template('four_oh_four.html'), 404
