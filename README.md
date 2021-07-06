Output the Windows domain computer list.
  1. Go to a DC or a pc with RSAT installed
  2. Import-Module ActiveDirectory
  3.get-adcomputer -filter *  | select name > pcList.csv 
  
  run the .ps1 script.
