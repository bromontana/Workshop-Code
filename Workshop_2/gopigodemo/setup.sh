#!/bin/bash

echo "Intiailzing..."

# Verify that some packages are installed
requirepackage(){
   if [ ! -z "$2" ] 
      then
         ldconfig -p | grep $2 > /dev/null
      else
         which $1 > /dev/null
   fi
   if [ $? != 0 ]
      then
         echo "Package $1: Installing..."
         apt-get install --assume-yes $1 > /dev/null
         echo "Package $1: Complete."
      else
         echo "Package $1: Already installed."
   fi
}
 
#Install Required Packages  
requirepackage git
requirepackage curl
sudo apt-get install -y build-essential

#Grab Latest Version of NodeJS
curl -sL https://deb.nodesource.com/setup_7.x | sudo -E bash -
sudo apt-get install -y nodejs

#Get GoPiGo Example Code
git clone https://github.com/DexterInd/GoPiGo
cd $PWD/GoPiGo/Setup
#Install Requirements
sudo bash install.sh

cd ../Software/Python
sudo python setup.py install

#Install Demo Dependencies
cd ../../../
cd $PWD/GoPiGoWebClient
sudo npm install

cd ../
cd $PWD/GoPiGoWebServer
sudo npm install

echo "Setup Complete!"
