#########################################################################################
# write a script to create a new csv file from DATA.csv file
# Script should take DATA.csv as arugment
# in new csv file should have 3 columns "Host Name", "Node IP", "Manufacturer" 
# cisco manufacturer node IP should have /24 subnet and brocade should have /32
#########################################################################################
import csv
with open(r'data.csv','r') as csv_file:
    csv_reader = csv.DictReader(csv_file)


    with open(r'iptest1','w') as new_file:
        fieldnames = ['Host Name','Node IP','Manufacturer']
        csv_writer = csv.DictWriter(new_file,fieldnames=fieldnames, extrasaction='ignore')
        csv_writer.writeheader()
        for line in csv_reader:
            if line['Manufacturer'] =="Brocade Systems":
                given_ip = (line['Node IP']).split("/")
                new_ip = given_ip[0]+'/'+'32'
                csv_writer.writerow({'Host Name':line['Host Name'],'Node IP':new_ip,'Manufacturer':line['Manufacturer']})
            elif line['Manufacturer'] =="Cisco Systems":
                given_ip = (line['Node IP']).split("/")
                new_ip = given_ip[0] + '/' + '24'
                csv_writer.writerow({'Host Name': line['Host Name'], 'Node IP': new_ip, 'Manufacturer': line['Manufacturer']})
            else:
                csv_writer.writerow(line)
