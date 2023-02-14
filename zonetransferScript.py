#!/usr/bin/python3

import subprocess

def run_dnsrecon(txt_file):
    with open(txt_file, 'r') as file:
        domains = file.readlines()
    with open("dnsreconDAoutput.txt", "w") as output:
        for domain in domains:
            result = subprocess.run(["dnsrecon", "-d", domain.strip(), "-a"], stdout=subprocess.PIPE)
            output.write(result.stdout.decode())

txt_file = "domain_list.txt"
run_dnsrecon(txt_file)
