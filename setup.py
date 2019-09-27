try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open("README.Md", 'r') as f:
    long_description = f.read()

with open('requirement.txt', 'r') as f:
    requirements = [line.strip() for line in f.readlines()]

setup(
   name='Wiki_scraper',
   version='1.0.0',
   description="Simple Python web scraping tool to scrap educational institutions details from Wikipedia using user input.",
   long_description=long_description,
   url='https://github.com/DSC-Galgotias/Wiki_Scraping.git',
   packages=['Wiki_Scraping'],
   install_requires=requirements
)
