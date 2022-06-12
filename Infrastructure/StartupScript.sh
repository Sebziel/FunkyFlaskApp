#!/bin/bash

sudo apt-get update -y
touch /home/ubuntu/install.log

echo \"START Java Installation\" >> /home/ubuntu/install.log
sudo apt install default-jre -y >> /home/ubuntu/install.log
sudo apt install default-jdk -y >> /home/ubuntu/install.log
echo \"END Java Installation\" >> /home/ubuntu/install.log
echo \"=====================\" >> /home/ubuntu/install.log
echo \"\" >> /home/ubuntu/install.log

echo \"START Jenkins Installation\" >> /home/ubuntu/install.log
curl -fsSL https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo tee /usr/share/keyrings/jenkins-keyring.asc > /dev/null
echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] https://pkg.jenkins.io/debian-stable binary/ | sudo tee /etc/apt/sources.list.d/jenkins.list > /dev/null
sudo apt-get update
sudo apt-get install jenkins -y >> /home/ubuntu/install.log
echo \"END Jenkins Installation\" >> /home/ubuntu/install.log


echo \"START awscli Installation\" >> /home/ubuntu/install.log
sudo apt install awscli -y >> /home/ubuntu/install.log
echo \"END awscli Installation\" >> /home/ubuntu/install.log

echo \"START pip and venv installation\" >> /home/ubuntu/install.log
sudo apt-get install pip -y >> /home/ubuntu/install.log
sudo apt-get install python3-venv -y >> /home/ubuntu/install.log
