#!/bin/bash

sudo yum install zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel \
openssl-devel xz xz-devel libffi-devel findutils git curl

curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash

echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> ~/.bash_profile
echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bash_profile

eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

pyenv install 2.7.16 && pyenv virtualenv 2.7.16 virtenv2716
pyenv install 3.7.3 && pyenv virtualenv 3.7.3 virtenv373


