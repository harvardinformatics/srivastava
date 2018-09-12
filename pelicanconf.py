#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime
from dateutil.tz import tzlocal

PLUGIN_PATHS = []
PLUGINS = []

AUTHOR = u'Andrew Gehrke'
SITENAME = u'Srivastava Lab Hofstenia miamia data'
SITEURL = 'http://srivastavalab.rc.fas.harvard.edu'
BANNER = True
BANNER_ALL_PAGES = False
DISPLAY_PAGES_ON_MENU = True
FAVICON = 'favicon.ico'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
FEED_ALL_RSS = 'rss.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

SHOW_ARTICLE_AUTHOR = True

DISPLAY_RECENT_POSTS_ON_SIDEBAR = False
DISPLAY_TAGS_ON_SIDEBAR = False
DISPLAY_TAGS_INLINE = True
TAG_CLOUD_STEPS = 4
TAG_CLOUD_MAX_ITEMS = 100
HIDE_SIDEBAR = True
DISPLAY_CATEGORIES_ON_SIDEBAR = False
DISPLAY_CATEGORIES_ON_MENU = False

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

STATIC_PATHS = ['images', 'extra']
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
}

DIRECT_TEMPLATES = ['index']

CUTOFF_DATE = datetime(2090, 1, 1, 0, 0, 0, tzinfo=tzlocal())

LINKS = ('/extra/harvard.png', 'Srivastava Lab', 'http://www.srivastavalab.org/')