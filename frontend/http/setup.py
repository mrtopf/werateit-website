import sys
import os
import pkg_resources
import pymongo
import logbook
import datetime
import db

from quantumcore.storages import AttributeMapper
from quantumcore.resources import CSSResourceManager, css_from_pkg_stream
from quantumcore.resources import JSResourceManager, js_from_pkg_stream
from frontend.framework.utils import get_static_urlparser


JS = [
    js_from_pkg_stream(__name__, 'static/js/jquery-1.4.4.min.js', name="", merge=False, prio=1,),
    #js_from_pkg_stream(__name__, 'static/js/jquery.tools.min.js', name="", merge=False, prio=4,),
]

CSS = [
    css_from_pkg_stream(__name__, 'static/css/screen.css', merge=True, prio=1, auto_reload=True),
]

def setup(**kw):
    """initialize the setup"""
    settings = AttributeMapper()
    settings['css'] = CSSResourceManager(CSS, prefix_url="/css", auto_reload=True)
    settings['js'] = JSResourceManager(JS, prefix_url="/js", auto_reload=True)
    settings['staticapp'] = get_static_urlparser(pkg_resources.resource_filename(__name__, 'static'))
    
    settings['secret_key'] = "ci28228zs7s8c6c8976c89c7s6s8976cs87d6" #os.urandom(20)
    settings['log'] = logbook.Logger("frontend")
    settings.update(kw)
    settings.mdb = mdb = pymongo.Connection().werateit
    settings.domain_db = db.Domains(mdb, "domains")
    return settings






