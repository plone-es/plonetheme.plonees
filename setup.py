from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='plonetheme.plonees',
      version=version,
      description="Theme for the Plone.es website",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='Danilo Dellaquila',
      author_email='ddellaquila@gmail.com',
      url='https://github.com/plone-es/plonetheme.plonees',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['plonetheme'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.app.theming',
          'plone.app.themingplugins',
      ],
      extras_require={
        'test': ['plone.app.testing',]
      },
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
# uncomment these to re-enable support for Paster local commands
#      setup_requires=["PasteScript"],
#      paster_plugins=["ZopeSkel"],
      )
