#!/usr/bin/env python
# coding: utf-8

import pocket
import yaml
import os
from pathlib import Path

if __name__ == '__main__':
    file = Path(os.environ.get('HOME')) / 'pocket.yml'

    with open(str(file)) as f:
        data = yaml.safe_load(f)
        consumer_key = data.get('consumer_key')
        access_token = data.get('access_token')
    p = pocket.Pocket(consumer_key, access_token)
    r = p.get(count=1)
    print(type(r))
