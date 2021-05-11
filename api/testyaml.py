# -*- coding: utf-8 -*-
"""
Created on Tue May 11 09:52:27 2021

@author: admin
"""

import yaml
env=yaml.safe_load(open("../api/env.yaml"))
print(env["testing-status"][env["default"]])
