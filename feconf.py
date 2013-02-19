# Copyright 2012 Google Inc. All Rights Reserved.
# Author: Sean Lip

"""Stores various configuration options for Oppia."""

import os
import jinja2

# Whether to unconditionally log info messages.
DEBUG = False

# Whether we are running in production mode.
PRODUCTION_MODE = False

# Whether we should serve the development or production experience.
DEV = (os.environ.get('SERVER_SOFTWARE')
       and os.environ['SERVER_SOFTWARE'].startswith('Development')
       and not PRODUCTION_MODE)

# The directory containing the HTML/JS/CSS templates.
TEMPLATE_DIR = 'templates/dev/head' if DEV else 'templates/prod/head'

# The directory containing third-party files.
THIRD_PARTY_DIR = 'third_party'

# The directories containing sample classifiers, explorations and widgets.
SAMPLE_CLASSIFIERS_DIR = 'data/classifiers'
SAMPLE_EXPLORATIONS_DIR = 'data/explorations'
SAMPLE_WIDGETS_DIR = 'data/widgets'

# The jinja environment used for loading frontend templates.
JINJA_ENV = jinja2.Environment(loader=jinja2.FileSystemLoader(
    os.path.join(os.path.dirname(__file__), TEMPLATE_DIR)))

# The jinja environment used for loading widget previews.
WIDGET_JINJA_ENV = jinja2.Environment(loader=jinja2.FileSystemLoader(
    os.path.join(os.path.dirname(__file__), SAMPLE_WIDGETS_DIR)))

# List of filepaths to JS libraries in third_party to include in responses.
THIRD_PARTY_JS_LIBS = [
    'jquery/jquery.min.js',
    'jqueryui/jquery-ui.min.js',
    'bootstrap/js/bootstrap.js',
    'angularjs/angular.min.js',
    'angularjs/angular-resource.min.js',
    'angularjs/angular-sanitize.min.js',
    'angular-ui/build/angular-ui.js',
    'd3js/d3.min.js',
]

# List of filepaths to CSS libraries to include in responses.
ALL_CSS_LIBS = [
    os.path.join(THIRD_PARTY_DIR, 'angular-ui/build/angular-ui.css'),
    os.path.join(THIRD_PARTY_DIR, 'bootstrap/css/bootstrap.css'),
    os.path.join(TEMPLATE_DIR, 'css/oppia.css'),
    os.path.join(THIRD_PARTY_DIR, 'bootstrap/css/bootstrap-responsive.css'),
]
