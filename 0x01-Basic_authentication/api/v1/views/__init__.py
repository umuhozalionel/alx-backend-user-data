#!/usr/bin/env python3
from api.v1.views.blueprint import app_views
import api.v1.views.index
import api.v1.views.users  # If this file exists
from models.user import User

User.load_from_file()
