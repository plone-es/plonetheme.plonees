# -*- coding: utf-8 -*-
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets import ViewletBase

SPANISH_COMMUNITIES = [
                       { 'code': 'cl', 'title': 'Plone Chile',     'url': 'http://www.plonechile.cl'},
                       { 'code': 'es', 'title': 'Plone España',    'url': 'http://plone.es/espana'},
                       { 'code': 'mx', 'title': 'Plone México',    'url': 'http://plone.mx'},
                       { 'code': 've', 'title': 'Plone Venezuela', 'url': 'http://plone.org.ve'},
                       { 'code': 'conosur', 'title': 'Plone Cono Sur', 'url': 'http://plone.org/countries/conosur/index_html'},
                      ]

class SlimbarViewlet(ViewletBase):
    index = ViewPageTemplateFile('slimbar.pt')

    def update(self):
        self.communities = SPANISH_COMMUNITIES
