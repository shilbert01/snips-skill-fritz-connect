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

class FritzConnect:
	def __init__(self, ipaddress, user, password):
		if ipaddress is not None:
		    self.ip = ipaddress
		else:
		    self.ip =fritzconnection.FRITZ_IP_ADDRESS,
		self.port=fritzconnection.FRITZ_TCP_PORT,
		# usually there is no username, seperate user/password can however be defined in the Fritz!Box webinterface
		if username is not None:
		    self.user = user
		else:
		    self.user = fritzconnection.FRITZ_USERNAME,
		self.password = password,

	fc = None
        if fc is None:
            fc = fritzconnection.FritzConnection(self.ip, self.port, self.user, self.password)
        self.fc = fc

	def dial_number(self, phonenumber):
		kwargs = {"NewX_AVM-DE_PhoneNumber":phonenumber[0]}
		#result = self.fc.call_action(ONTEL_SERVICE, ACTION, **kwargs)
		result = self.fc.call_action('X_VoIP', 'X_AVM-DE_DialNumber', **kwargs)
		#todo; extract and return status code (e.g. 200),
