"""Generate Secular Humanist of NY style.
"""

# $Id: ShsnyGenerator.py,v 1.5 2007/03/10 19:33:37 colin Exp $

import os
import time

from Skeleton import Skeleton
from Sidebar import Sidebar, BLANKCELL
from Banner import Banner
from HTParser import HTParser
from LinkFixer import LinkFixer


sitelinks = [
    ('%(rootdir)s/index.html',          'Home'),
    ('%(rootdir)s/pique/index.html',    'PIQUE &mdash; SHSNY Newsletter'),
    ('%(rootdir)s/about.html',          'About Us'),
    ('%(rootdir)s/whatis.html',         'What Is Secular Humanism?'),
    ('%(rootdir)s/member.html',         'Membership'),
    ('%(rootdir)s/affirmations.html',   'Affirmations of Humanism'),
    ('%(rootdir)s/contact.html',        'Contact Us'),
    ]


class ShsnyGenerator(Skeleton, Sidebar, Banner):
    def __init__(self, file, rootdir, relthis):
        self.__body = None
        root, ext = os.path.splitext(file)
        html = root + '.html'
        p = self.__parser = HTParser(file)
        f = self.__linkfixer = LinkFixer(html, rootdir, relthis)
        p.process_sidebar()
        p.sidebar.append(BLANKCELL)
        # massage our links
        self.__d = {'rootdir': rootdir}
        self.__linkfixer.massage(p.sidebar, self.__d)
        Sidebar.__init__(self, p.sidebar)
        #
        # fix up our site links, no relthis because the site links are
        # relative to the root of my web pages
        #
        sitelink_fixer = LinkFixer(f.myurl(), rootdir)
        sitelink_fixer.massage(sitelinks, self.__d, aboves=1)
        Banner.__init__(self, sitelinks, cols=2)

    def get_corner(self):
        return ''

    def get_corner(self):
        rootdir = self.__linkfixer.rootdir()
        return '''
<center>
    <a href="%(rootdir)s/index.html">
      <img src="%(rootdir)s/SHSNY.gif" alt="SHSNY Main Page" width=113 height=86/>
    </a>
</center>''' \
    % self.__d

    def get_corner_bgcolor(self):
        return 'black'

    def get_banner(self):
        return Banner.get_banner(self)

    def get_title(self):
        return self.__parser.get('title')

    def get_sidebar(self):
        return Sidebar.get_sidebar(self)

    def get_banner_attributes(self):
        return 'CELLSPACING=0 CELLPADDING=0'

    def get_body(self):
        if self.__body is None:
            self.__body = self.__parser.fp.read()
        return self.__body

# end ShsnyGenerator.py
