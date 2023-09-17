#!/bin/bash

sudo apt update -y
sudo apt upgrade -y
sudo apt install -y curl wget vim git unzip
sudo apt install -y unattended-upgrades
sudo dpkg-reconfigure -plow unattended-upgrades
sudo apt install git

install_chrome() {
    echo "Installing Google Chrome..."
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -P /tmp
    sudo dpkg -i /tmp/google-chrome-stable_current_amd64.deb
    sudo apt-get -f install -y
    rm /tmp/google-chrome-stable_current_amd64.deb
    echo "Google Chrome is installed."
}

remove_firefox() {
    echo "Removing Mozilla Firefox..."
    sudo apt-get remove --purge firefox -y
    sudo apt-get autoremove -y
    sudo rm -rf ~/.mozilla
    echo "Mozilla Firefox is removed."
}

create_new_user() {
    read -p "Enter the username for the new user: " username
    read -s -p "Enter the password for the new user: " password
    echo
    sudo useradd -m -s /bin/bash $username
    echo "$username:$password" | sudo chpasswd
    echo "User $username is created."
}


read -p "Do you want to install Google Chrome? (y/n): " install_choice
if [[ "$install_choice" == "y" || "$install_choice" == "Y" ]]; then
    install_chrome
fi

read -p "Do you want to remove Mozilla Firefox? (y/n): " remove_choice
if [[ "$remove_choice" == "y" || "$remove_choice" == "Y" ]]; then
    remove_firefox
fi

read -p "Do you want to create a new user? (y/n): " create_user_choice
if [[ "$create_user_choice" == "y" || "$create_user_choice" == "Y" ]]; then
    create_new_user
fi