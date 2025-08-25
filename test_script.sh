#!/usr/bin/env bash
source ./quantium/bin/activate
pytest test_app.py ; echo "Error code: $?"
