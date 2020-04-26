# Assignment_TimesInternet

Instructions text file is provided in each assignment
# Assignment_1
  --> Goto the path where elkstack.yaml file is available.

  --> vars/all.yaml is not having kibana_version(commented) value. That need to
    be passed during the playbook exection.
  --> Run the below command: (Kibana version which need to be installed)

    ansible-playbook -i inventory --extra-vars "kibana_version=6.5.4" elkstack.yaml
   
  --> Make sure the user is priviledged to perform the task.

  --> Change the ip/user name inventory and other files 
  

# Assignment_2
  --> Make sure you add the access_key_id and secret_access_key before executing the same.
 
  --> Python3 is being used to compile the program.
  
  --> .csv file will be created where python is installed
# Assignment_3
  --> Goto Docker_Image_Setup folder
  
  --> run the docker build command
  
    docker build --tag my-python-app .
    
  --> Go to main path and locate deployment.yaml file
  
  --> run the below command on master server of k8s cluster
  
       kubectl apply -f deployment.yaml
       
  --> Addition resource will be created to fulfill the last requirement (Pod scale : At CPU utilisation > 50% from 1 to 5           pods)
  
       horizontalpodautoscaler.autoscaling/my-python-app
       
  --> curl the localhost:5000 , Application response will be displayed.
