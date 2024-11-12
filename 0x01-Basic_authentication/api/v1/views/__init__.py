#!/usr/bin/env python3
from models.user import User
from api.v1.views.blueprint import app_views

import api.v1.views.index
import api.v1.views.users  # If this file exists

User.load_from_file()
