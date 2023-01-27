#!/bin/bash

# Cleaning
echo " > Cleaning..."
sudo rm -fr /var/www/html/soap/php/p2.php
sudo rm -fr /var/www/html/soap/php/p2.wsdl
echo "   Cleaned."
    
# Setting up
echo " > Setting up..."
sudo cp ./p2.php /var/www/html/soap/php/p2.php
sudo cp ./p2.wsdl /var/www/html/soap/php/p2.wsdl
echo "   Set up."
