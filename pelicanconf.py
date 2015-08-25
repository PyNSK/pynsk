#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

from embedly_cards import EmbedlyCardExtension
from pyembed.markdown import PyEmbedMarkdown

PROJECT_DIR = os.path.normpath(
    os.path.abspath(os.path.dirname(os.path.abspath(__file__))))


def get_theme_path(theme_name):
    return os.path.join(PROJECT_DIR, 'themes', theme_name)

AUTHOR = 'Alexander Sapronov'
SITENAME = 'PyNSK - Новосибирское Python сообщество'
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

SUMMARY_MAX_LENGTH = 60
MD_EXTENSIONS = ['codehilite(css_class=highlight)',
                 'extra',
                 # ...
                 EmbedlyCardExtension(),
                 PyEmbedMarkdown()]

# Social widget
SOCIAL = (
    ('vk', 'https://vk.com/pynsk', '<b>Группа в ВКонтакте</b>'),
    ('slack', 'https://gitter.im/PyNSK/PyNSK', '<b>Наш Чат</b>'),
    ('twitter', 'https://twitter.com/py_nsk', 'В Twitter'),
    ('facebook', 'https://www.facebook.com/PyNskCom', 'Группа в Facebook'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

DIRECT_TEMPLATES = (
    ('index', 'tags', 'categories', 'authors', 'archives', 'search')
)
MARKUP = ('rst', 'markdown',)

THEME = get_theme_path('pelican-bootstrap3')


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
    'optimize_images',
    'tag_cloud',
    'post_stats',
    'related_posts',
    'embedly_cards',
    'pin_to_top',
]
ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'

ADDTHIS_PROFILE = True
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_CATEGORIES_ON_SIDEBAR = True
DISPLAY_TAGS_ON_SIDEBAR = True
SHOW_ARTICLE_CATEGORY = True
DISPLAY_ARTICLE_INFO_ON_INDEX = False
TAGS_URL = 'tags.html'
RELATED_POSTS_TEXT = 'Новости по теме:'
RELATED_POSTS_MAX = 10
ABOUT_ME = True
AVATAR = '/images/logo.png'
DISPLAY_TAGS_INLINE = True

# todo
# когда напишу страницы, то включить обрабтно
DISPLAY_PAGES_ON_MENU = False

GOOGLE_ANALYTICS = 'UA-53909016-3'
GITHUB_URL = 'https://github.com/WarmongeR1/pynsk'



MENUITEMS = [
    ('Категории', '/categories.html'),
]
