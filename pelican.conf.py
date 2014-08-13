#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'Roberto Segebre'
DISQUS_SITENAME = 'rsegebre'
SITENAME = u"foodie rsegebre"
SITEURL = 'http://foodie.rsegebre.com'
#SITELOGO = 'static/images/favicon.ico'

TIMEZONE = "America/New_York"
LOCALE = ""

FEED_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feed/%s.rss.xml'
GITHUB_URL = 'http://github.com/rsegebre'
#GOOGLE_ANALYTICS = 'UA-32786140-1'
DEFAULT_LANG='en'
DISPLAY_TAGS_ON_SIDEBAR = True
DISPLAY_CATEGORIES_ON_SIDEBAR = True
#RELATIVE_URLS = True

#Theme
THEME = '/Users/rsegebre/Documents/Projects/theme/pelican-elegant-1.3'

# Blogroll
LINKS =  (
    ('Colgate COSC Dept. Website', 'http://cs.colgate.edu'),
    ('Coding Horror Blog by Jeff Atwood', 'http://www.codinghorror.com/blog/')
         )

# Social widget
SOCIAL = (
          ('twitter', 'http://twitter.com/rss1989'),
          ('github', 'http://github.com/rsegebre'),
          ('facebook', 'http://www.facebook.com/rsegebre'),
          ('linkedIn',
'http://www.linkedin.com/pub/roberto-segebre/40/8b1/6b2'),
         )

# Elegan configuration variables
PLUGIN_PATH = '/Users/rsegebre/Documents/Projects/pelican-plugins'
PLUGINS = ['sitemap', 'extract_toc', 'tipue_search']
MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'headerid', 'toc']
DIRECT_TEMPLATES = (('index', 'tags', 'categories','archives', 'search',
'404'))
STATIC_PATHS = ['theme/images', 'images']
TAG_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
AUTHOR_SAVE_AS = ''

#SITEMAP
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}


TWITTER_USERNAME = 'rss1989'
ADDTHIS_PROFILE = 'ra-52d5e9e5415eda76'

DEFAULT_PAGINATION = 5
