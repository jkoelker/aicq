"""
Created September 6, 2012

@author: Justin Hammond, Rackspace Hosting
"""

import logging
import json

import aiclib
from quantum.common import exceptions as exception
from quantum.openstack.common import jsonutils

LOG = logging.getLogger("aicq-nvplib")
LOG.setLevel(logging.INFO)

_nvp = None

"""
basic functionality here
"""


def _conn(controller):
    global _nvp
    if _nvp is None:
        _nvp = aiclib.nvp.Connection(controller)
    return _nvp

"""
Network (lswitch) functions
"""


def get_network(controller, net_id):
    try:
        resp = _conn(controller).lswitch(net_id).read()
    except LookupError:
        raise exception.NetworkNotFound(net_id=net_id)
    except Exception:
        raise exception.QuantumException()
    LOG.debug("Got networking \"%s\": %s" % (net_id, resp))
    return resp


def test_except_network():
    #TODO: Put this into a test
    return get_network("http://nvp", "*")


def test_fail_network():
    #TODO: Put this into a test
    return get_network("https://nvp", "*")


def test_get_network():
    #TODO: Put this into a test
    return get_network("https://nvp", "101661a7-b5d1-4ee6-b443-1d81dfaf4b81")

"""
Port (lport) functions
"""
