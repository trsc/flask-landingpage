#!/bin/bash
# Displays a dump of the sqlite database
# Requires sqlite3 to be installed


echo -e '.mode column\n select * from signup;' | sqlite3 signups.db
