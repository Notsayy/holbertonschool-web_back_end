#!/usr/bin/env python3
"""Flask app with locale and timezone inference from URL, user, or default."""
from flask import Flask, g, render_template, request
from flask_babel import Babel
import pytz


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """App configuration with supported languages and Babel defaults."""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel()


def get_user():
    """Return user dict from login_as parameter or None if not found."""
    try:
        user_id = int(request.args.get('login_as'))
        return users.get(user_id)
    except (TypeError, ValueError):
        return None


@app.before_request
def before_request():
    """Set the current user as a global before each request."""
    g.user = get_user()


def get_locale():
    """Determine locale with priority: URL > user > header > default."""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale

    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user.get('locale')

    best = request.accept_languages.best_match(app.config['LANGUAGES'])
    if best:
        return best

    return app.config['BABEL_DEFAULT_LOCALE']


def get_timezone():
    """Determine timezone with priority: URL > user > default UTC."""
    timezone = request.args.get('timezone')
    if timezone:
        try:
            return pytz.timezone(timezone).zone
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    if g.user and g.user.get('timezone'):
        try:
            return pytz.timezone(g.user.get('timezone')).zone
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    return app.config['BABEL_DEFAULT_TIMEZONE']


babel.init_app(
    app,
    locale_selector=get_locale,
    timezone_selector=get_timezone
)


@app.route('/')
def index():
    """Render the index page."""
    return render_template('7-index.html')
