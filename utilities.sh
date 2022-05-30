#!/bin/bash

#Script should be executed with . space notation to set the variables in caller's shell
#Copy paste below command: 
# ". utilities.sh"

PS3='Choose option: '

select option in "set environment varibles" "Generate requirements.txt" quit
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
            pip list | awk '{print $1}' | sed '1,2d' > requirements.txt
            ;;
        quit)
            echo "User requested quit"
            echo "selected option: $option"
            echo "selected number: $REPLY"
            break
            ;;
    esac
done