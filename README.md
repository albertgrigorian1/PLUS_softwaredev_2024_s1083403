Workflow for the Task: Recreating Environments

1. Preparation and Download
   
Download .yml Files: I'll simply download the required .yml files directly from the repository. This will be done from the repository's main page where files are listed, usually with a download option.
![image](https://github.com/albertgrigorian1/PLUS_softwaredev_2024_s1083403/assets/92171413/cc445008-97bf-450c-b7d1-02f57d4b4bc6)


3. Recreate Environments
Navigate to Directory: I'll open my terminal and navigate to the directory where I've saved the downloaded .yml files.
![image](https://github.com/albertgrigorian1/PLUS_softwaredev_2024_s1083403/assets/92171413/c0f61ff2-a50b-4426-827e-5c4bdfe56ebd)


Create Environments: Using Conda, I'll recreate the environments specified in the .yml files. I'll execute the  command conda env create -f environment.yml for each file. This will set up the environments as defined by the .yml files.
![image](https://github.com/albertgrigorian1/PLUS_softwaredev_2024_s1083403/assets/92171413/6042488a-c9e5-40ff-9e1d-59d28e029416)



Activate Environments: Once the environments are successfully created, I'll activate them by using conda activate environment_name, where "environment_name" is the name specified within the .yml file.
![image](https://github.com/albertgrigorian1/PLUS_softwaredev_2024_s1083403/assets/92171413/ae2705ec-0fca-4717-81b7-418cc624f1a5)


5. Conclusion

The recreation of the environments using the provided .yml files was overall successful. I was able to recreate both environments without any errors. While the setup of the first environment was quick and went smoothly, I noticed that the process for the second .yml file took longer. This could be due to specific dependencies or configurations in the second file that required more time to resolve. Despite this delay, everything functioned flawlessly in the end.
