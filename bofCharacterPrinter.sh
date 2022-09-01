#! /bin/bash

#simple user interaction to get whatever character they want to print and how many times. 
read -p "What would you like to print? " letter
read -p "How many times? " times

#yes i am using python and not python3 (i'll fix this later) 
python -c "print '$letter' * $times"
