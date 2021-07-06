 #run these two commands on a DC or a PC with RSAT installed
#Import-Module ActiveDirectory
#get-adcomputer -filter *  | select name > pcList.csv 

#set the path of the file with the domain listing
$computers = Get-Content -Path .\pcList.csv
$results = ForEach ($computer in $computers) 
{
    $sess = New-PSSession -ComputerName $computer.Trim();
    Invoke-Command -ScriptBlock{get-Service Spooler} -Session $sess
}

$results > test.csv 
