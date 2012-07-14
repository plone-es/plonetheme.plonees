import unittest2 as unittest
import transaction

from plonetheme.plonees.testing import PLONEES_THEME_INTEGRATION_TESTING
from plonetheme.plonees.testing import PLONEES_THEME_FUNCTIONAL_TESTING

from plone.testing.z2 import Browser
from plone.app.testing import SITE_OWNER_NAME
from plone.app.testing import SITE_OWNER_PASSWORD

from zope.component import getUtility
from Products.CMFCore.utils import getToolByName

from plone.registry.interfaces import IRegistry
from plone.app.theming.interfaces import IThemeSettings

class TestSetup(unittest.TestCase):

    layer = PLONEES_THEME_INTEGRATION_TESTING

    def test_css_registry_configured(self):
        portal = self.layer['portal']
        cssRegistry = getToolByName(portal, 'portal_css')
        self.assertTrue("++theme++plonetheme.plonees/css/plone-es.css"
                in cssRegistry.getResourceIds()
            )

    def test_theme_configured(self):
        registry = getUtility(IRegistry)
        settings = registry.forInterface(IThemeSettings)
        self.assertEqual(settings.enabled, True)
        self.assertEqual(settings.rules,
                "/++theme++plonetheme.plonees/rules.xml"
            )
        self.assertEqual(settings.absolutePrefix,
                "/++theme++plonetheme.plonees"
            )

class TestRendering(unittest.TestCase):

    layer = PLONEES_THEME_FUNCTIONAL_TESTING

    def test_render_plone_page(self):
        app = self.layer['app']
        portal = self.layer['portal']

        transaction.commit()

        browser = Browser(app)

        browser.open(portal.absolute_url())
        self.assertTrue('<div id="visual-portal-wrapper">' in browser.contents)

    def test_render_zmi_page(self):
        app = self.layer['app']
        portal = self.layer['portal']

        transaction.commit()

        browser = Browser(app)
        browser.addHeader('Authorization', 'Basic %s:%s' % (SITE_OWNER_NAME, SITE_OWNER_PASSWORD,))

        browser.open(portal.absolute_url() + '/manage_main')

        self.assertFalse('<div id="visual-portal-wrapper">' in browser.contents)
