#run these two commands on a DC or a PC with RSAT installed
#1. Import-Module ActiveDirectory
#2. get-adcomputer -filter *  | select name > pcList.csv 

#set the path of the file with the domain listing
$computers = Get-Content -Path .\pcList.csv

#run through each item in the list
$results = ForEach ($computer in $computers) 
{
#create a PS remote session to each computer and get the status of the Spooler Service
    $sess = New-PSSession -ComputerName $computer.Trim();
    Invoke-Command -ScriptBlock{get-Service Spooler} -Session $sess
}
#print the results out to a csv
$results > results.csv 
