#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

PROJECT_DIR = os.path.normpath(
    os.path.abspath(os.path.dirname(os.path.abspath(__file__))))


def get_theme_path(theme_name):
    return os.path.join(PROJECT_DIR, 'themes', theme_name)


themes = [
    'aboutwilson',
    'alchemy',
    'elegant',
    'foundation-default-colours',
    'lazystrap',
    'Nuja',
    'pelican-bootstrap3',
    'pelican-twitchy']

AUTHOR = 'Alexander Sapronov'
SITENAME = 'PyNSK - Новосибирское Python сообщесщество'
# SITEURL = 'http://pynsk.ru'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Novosibirsk'

DEFAULT_LANG = 'ru'

# Feed generation is usually not desired when developing
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('Pelican', 'http://getpelican.com/'),
    ('Python.org', 'http://python.org/'),
    ('Jinja2', 'http://jinja.pocoo.org/'),
    ('You can modify those links in your config file', '#'),
)

# Social widget
SOCIAL = (
    ('twitter', 'https://twitter.com/py_nsk'),
    ('facebook', 'https://www.facebook.com/PyNskCom'),
    ('vk', 'https://vk.com/pynsk'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True


SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.7,
        "indexes": 0.5,
        "pages": 0.3,
    },
    "changefreqs": {
        "articles": "monthly",
        "indexes": "daily",
        "pages": "monthly",
    }
}

PLUGIN_PATHS = [
    'pelican-plugins',
]

PLUGINS = [
    'summary',
    'liquid_tags.img',
    'liquid_tags.video',
    'liquid_tags.include_code',
    'liquid_tags.notebook',
    'liquid_tags.literal',
    'tipue_search',
    'sitemap',
    # 'pelican_youtube',
    'optimize_images',

]

DIRECT_TEMPLATES = (
    ('index', 'tags', 'categories', 'authors', 'archives', 'search')
)
MARKUP = ('rst', 'markdown',)
THEME = get_theme_path(themes[2])
