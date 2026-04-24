#!/usr/bin/env python3
"""Flask app with Babel i18n using gettext for template parametrization."""
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
    """Determine the best locale from the request Accept-Language header."""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel.init_app(app, locale_selector=get_locale)


@app.route('/')
def index():
    """Render the index page."""
    return render_template('3-index.html')
