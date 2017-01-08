from os.path import exists
from shutil import rmtree
from selenium import webdriver
from flask_page import pages
from threading import Thread


def before_feature(context, feature):
    if 'web' in feature.tags:
        context.thread = Thread(target=pages.start_flask)
        context.thread.start()
        context.browser = webdriver.Firefox()


def after_feature(context, feature):
    if 'web' in feature.tags:
        pages.shutdown()
        context.browser.quit()


def after_all(context):
    path = './tmp'
    if exists(path):
        rmtree(path)
