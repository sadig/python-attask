# -*- coding: utf-8 -*-
###############################################################################
# python-foreman-api - Foreman API Python Library
# Copyright (C) 2012 Stephan Adig <sh@sourcecode.de>
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301 USA
###############################################################################

import sys
import json

try:
    from restkit import Resource
except ImportError, e:
    print('You didn\'t install python-restkit library')
    print(e)
    sys.exit(1)

class AttaskResource(Resource):
    """Subclass of Restkits Resource Class"""

    def __init__(self, url=None, pool_instance=None, **kwargs):
        """Constructor
        
        :param url: Foreman URL
        :type url: str
        :inherits: Resource.__init__ parameters
        
        """
        super(AttaskResource, self).__init__(url, follow_redirect=True,
                                     max_follow_redirect=10,
                                     pool=pool_instance,
                                     **kwargs)

    def request(self, *args, **kwargs):
        """RestKIT Resource Request Method
        
        is only adding additional headers for Foreman
        """
        headers = {'Content-Type':'application/json',
                   'Accept':'application/json'}
        kwargs['headers'] = headers
        resp = super(AttaskResource, self).request(*args, **kwargs)
        return json.loads(resp.body_string())


