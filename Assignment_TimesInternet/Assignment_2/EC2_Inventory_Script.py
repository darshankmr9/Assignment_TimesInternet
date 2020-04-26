import boto3
import csv
from pprint import pprint
#Don't pass region_name if all region's details is demanded
ec2_resource_object = boto3.resource('ec2', aws_access_key_id="***********", aws_secret_access_key ="*************")
header_csv=['Serial_No','InstanceID','InstanceType','InstancePrivateIP','InstancePublicIP','InstanceHypervisor','InstanceSubnet']
Serial_No=1
file_object = open("ec2-Inventory-details.csv","w")
csv_w=csv.writer(file_object)
csv_w.writerow(header_csv)
for each_in_list in ec2_resource_object.instances.all():
    Ins_ID=each_in_list.instance_id
    Ins_Type=each_in_list.instance_type
    Ins_Private_Ip=each_in_list.private_ip_address
    Ins_Public_Ip=each_in_list.public_ip_address
    Ins_Hypervisor=each_in_list.hypervisor
    Ins_Subnet=each_in_list.subnet
    print(Serial_No,Ins_ID,Ins_Type,Ins_Private_Ip,Ins_Public_Ip,Ins_Hypervisor,Ins_Subnet)
    csv_w.writerow([Serial_No,Ins_ID,Ins_Type,Ins_Private_Ip,Ins_Public_Ip,Ins_Hypervisor,Ins_Subnet])
    Serial_No=Serial_No+1
file_object.close()
