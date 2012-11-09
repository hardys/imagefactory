#
#   Copyright 2012 Red Hat, Inc.
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http:/www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

from imgfac.ApplicationConfiguration import ApplicationConfiguration
from imgfac.rest.OAuthTools import validate_two_leg_oauth

class Consumer(object):
    def __init__(self, key):
        consumers = ApplicationConfiguration().configuration['clients']
        self.key = key
        self.secret = consumers.get(key) if consumers else None

def auth_protect(f):
    def decorated_function(*args, **kwargs):
        if(not ApplicationConfiguration().configuration['no_oauth']):
            validate_two_leg_oauth()
        return f(*args, **kwargs)
    decorated_function.__name__ = f.__name__
    return decorated_function
