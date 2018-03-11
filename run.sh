#!/bin/sh

export FLASK_APP='trackem/run.py';
export FLASK_DEBUG=1;

flask run