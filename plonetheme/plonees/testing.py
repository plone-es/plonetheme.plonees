from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

from zope.configuration import xmlconfig

class PloneesTheme(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import plonetheme.plonees
        xmlconfig.file('configure.zcml', plonetheme.plonees, context=configurationContext)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'plonetheme.plonees:default')

PLONEES_THEME_FIXTURE = PloneesTheme()
PLONEES_THEME_INTEGRATION_TESTING = IntegrationTesting(bases=(PLONEES_THEME_FIXTURE,), name="PloneesTheme:Integration")
PLONEES_THEME_FUNCTIONAL_TESTING = FunctionalTesting(bases=(PLONEES_THEME_FIXTURE,), name="PloneesTheme:Functional")
