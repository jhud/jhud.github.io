#!/bin/sh
nodemon --watch ../src --exec "python3" build_static_site.py -e htm,html,j2
