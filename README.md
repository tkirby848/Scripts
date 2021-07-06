Output the Windows domain computer list.
  1. Go to a DC or a pc with RSAT installed
  2. Import-Module ActiveDirectory
  3. get-adcomputer -filter *  | select name > pcList.csv 
  
  run the .ps1 script.
  
  Filenames and locations can be changed in the script to make it work better for you! 
  This script can be used before and after making GPO changes, or used randomly. 
