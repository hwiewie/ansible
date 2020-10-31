#!/bin/bash

source "${SH_LIBRARY_PATH}/common.sh"
source "${SH_LIBRARY_PATH}/githubapi.sh"

check_env REPOSITORY PULL_REQUEST_VARIANT

DIR=$(dirname ${BASH_SOURCE[0]})
NAME=$(basename -s ".sh" ${BASH_SOURCE[0]})

githubapi_setup_environment

log_must mkdir -p "$REPOSITORY"

log_must ruby "${DIR}/${NAME}.rb" \
    --pull-requests-file "$REPOSITORY/pull-requests.json" \
    --netrc-file netrc-file \
    --repository "$REPOSITORY" \
    --pull-request-variant "$PULL_REQUEST_VARIANT"

# vim: tabstop=4 softtabstop=4 shiftwidth=4 expandtab textwidth=72 colorcolumn=80
