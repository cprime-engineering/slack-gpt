#!/usr/bin/env bash

# Update apt-get ----------------------------------------------------------------------------------------------
apt-get update

# install unzip -----------------------------------------------------------------------------------------------
apt-get -y install unzip --no-install-recommends

# Install python tools ----------------------------------------------------------------------------------------
apt-get -y install python3-venv python3-pip python3-dev --no-install-recommends

# Install golang ----------------------------------------------------------------------------------------------
add-apt-repository -y ppa:longsleep/golang-backports
apt-get update
apt-get -y install golang --no-install-recommends

# install bash-completion -------------------------------------------------------------------------------------
apt-get -y install bash-completion --no-install-recommends