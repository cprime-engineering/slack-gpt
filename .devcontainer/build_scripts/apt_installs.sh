#!/usr/bin/env bash

# Update apt-get ----------------------------------------------------------------------------------------------
apt-get update

# install unzip -----------------------------------------------------------------------------------------------
apt-get -y install unzip --no-install-recommends

# Install python tools ----------------------------------------------------------------------------------------
apt-get -y install python3-venv python3-pip python3-dev --no-install-recommends

# Install golang ----------------------------------------------------------------------------------------------
cd /tmp
wget https://go.dev/dl/go1.17.5.linux-amd64.tar.gz
tar -C /usr/local -xzf go1.17.5.linux-amd64.tar.gz
cd /

# install bash-completion -------------------------------------------------------------------------------------
apt-get -y install bash-completion --no-install-recommends
