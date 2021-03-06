#!/bin/bash

#Script should be executed with . space notation to set the variables in caller's shell
#Copy paste below command: 
# ". utilities.sh"

PS3='Choose option: '

select option in "set environment varibles" "Generate requirements.txt" "VmSetup" quit
do
    case $option in
        "set environment varibles" )
            echo "selected option: $option"
            echo "selected number: $REPLY"
            export FLASK_ENV=development
            echo "set up FLASK_ENV = " $FLASK_ENV
            export FLASK_APP=SimpleApp.py
            echo "set up FLASK_APP = " $FLASK_APP
            ;;
        "Generate requirements.txt")
            echo "selected option: $option"
            echo "selected number: $REPLY"
            pip3 freeze > requirements.txt
            ;;
        "VmSetup")
            echo "selected option: $option"
            echo "selected number: $REPLY"
            sudo apt-get update -y
            sudo apt-get install pip -y
            sudo apt-get install python3-venv -y
            python3 -m venv my_environment
            ;;
        quit)
            echo "User requested quit"
            echo "selected option: $option"
            echo "selected number: $REPLY"
            break
            ;;
    esac
done