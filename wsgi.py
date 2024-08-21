import sys
import os

sys.path.insert(0, '/home2/rftboymy/public_html/website_1194c547')

activate_this = '/home2/rftboymy/public_html/website_1194c547/venv/bin/activate_this.py'
exec(open(activate_this).read(), {'__file__': activate_this})

from server import app as application

