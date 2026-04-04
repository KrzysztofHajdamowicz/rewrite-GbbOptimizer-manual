#!/bin/bash
export PATH="/opt/homebrew/bin:$PATH"
exec hugo server "$@"
