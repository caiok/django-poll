#!/bin/bash

# Warning: this script is CentOS based

# -------------- #
cat >> /etc/profile.d/custom.sh << EOF 

export http_proxy=http://proxy.mmfg.it:8080

export https_proxy=\$http_proxy
export ftp_proxy=\$http_proxy
export HTTP_PROXY=\$http_proxy
export HTTPS_PROXY=\$http_proxy
export FTP_PROXY=\$http_proxy
export no_proxy=\$http_proxy

alias rm='rm -i'
alias cp='cp -i'
alias mv='mv -i'

EOF
# -------------- #

set -x

# -------------- #
source /etc/profile.d/custom.sh
# -------------- #

# -------------- #
yum update -y
yum install -y epel-release
yum update -y

yum install -y python-pip
pip install --upgrade pip
pip install --upgrade django
# -------------- #

# -------------- #
python -c "import django; print('Django Version: ' + django.get_version())"
# -------------- #