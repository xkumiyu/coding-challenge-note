exit_status=0

check () {
    if [ $1 = 0 ]; then
        printf '\033[32m%s\033[m %s\n' 'success:' $2
    else
        printf '\033[31m%s\033[m %s\n' 'error:' $2
        exit_status=1
    fi
}

# code
pipenv run flake8 algorithms >/dev/null 2>&1
check $? "flake8"

pipenv run black algorithms --check >/dev/null 2>&1
check $? "black"

pipenv run pytest --cov=algorithms --cov-report=html >/dev/null 2>&1
check $? "pytest"

# docs
yarn run markdownlint docs >/dev/null 2>&1
check $? "markdownlint"

yarn run textlint docs >/dev/null 2>&1
check $? "textlint"

exit $exit_status
