#!/usr/bin/env python3
"""Flask app with forced locale via URL parameter."""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """App configuration with supported languages and Babel defaults."""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel()


def get_locale():
    """Determine locale from URL parameter or Accept-Language header."""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel.init_app(app, locale_selector=get_locale)


@app.route('/')
def index():
    """Render the index page."""
    return render_template('4-index.html')
