#!/bin/env sh

curl https://xkcd.com/2445/switchboard.json > switchboard.json

sha256sum switchboard.json || true
