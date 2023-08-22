#!/bin/sh
nodemon --watch ../src --exec "python" build_static_site.py -e htm,html
