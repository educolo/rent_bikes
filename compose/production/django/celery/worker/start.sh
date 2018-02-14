#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset


celery -A rent_bikes.taskapp worker -l INFO
