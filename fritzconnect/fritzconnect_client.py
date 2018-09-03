import argparse
import os

# tiny hack to run this as a package but also from the command line. In
# the latter case ValueError is raised from python 2.7,
# SystemError from Python 3.5
# ImportError from Python 3.6

# This is not to be confused with the python libraty fritconnection which does all the heavy lifting

try:
    from . import fritzconnection
except (ValueError, SystemError, ImportError):
    import fritzconnection

from datetime import datetime, timedelta
from lxml import etree

class FritzConnect(object):
	def __init__(self, 
		fc = None,
		address=fritzconnection.fritzconnection.FRITZ_IP_ADDRESS,
		port=fritzconnection.fritzconnection.FRITZ_TCP_PORT,
		user=fritzconnection.fritzconnection.FRITZ_USERNAME,
		password=''):
	    super(FritzConnect, self).__init__()
	    if fc is None:
		fc = fritzconnection.FritzConnection(address, port, user, password)
	    self.fc = fc

	def dialNumber(self, phonenumber):
		kwargs = {"NewX_AVM-DE_PhoneNumber":phonenumber}
		result = self.fc.call_action('X_VoIP', 'X_AVM-DE_DialNumber', **kwargs)
		#todo; extract and return status code (e.g. 200),

	def getStatus(self):
		result = self.fc.call_action('X_VoIP', 'X_AVM-DE_DialNumber', **kwargs)