# CS 235 Lab 1 report

## Notes from Lab1

- **The benefits of using virtual environments to develop:**

    - Wo55vrking in distinct environments with their own distinct pacakages and python installation

    - Using virtual environments, we can use different versions of a package.
     
      - This is useful as major versions of software are not ussually backwards compatible.  

    - We can generate a file with all the package requirements easier. 

- **We learnt how to set up a virtual environment using conda- a package and virtual enviroment manager:**

    > Creation of an enviroment: 
            
        conda create -n environmentName python=python_version

    > Activation of an environment: <code></code>
    
        conda activate environmentName

    > Install packages to a virtual enviroment

        conda install -c channelName package1 package2 
    > Deactivation of an environment:

        conda deactivate environmentName
        

- **Miscellaneous**

    - Git is a widely used version controll system. 

        - Github is a hosting platform for repository for collabrative projects. 
    - Markdown is a markup langauge most commonly used to write README.md files git up repositories.
    - The Breakpoint() function in python is useful for debugging; especially with the help of vs codes variable  
  ---
  ## Reflection

  **What I learnt:**
        
    - I learnt about how and why one would want to employ a virtual environment to develop code in. 
    - I learnt that conda is a system that allows the creation and management of such virtual environments. 
      - It does this by partitioning a portion of the drive and reserving it for virtualization when the enviroment is active
    
    **Hands on tasks:**
    1. Task 1: Create a virtual environment with Conda.
        
        - Encountered an HTTP conncection failure after downloading conda and trying to set up a virtual environment. 
            
        ![image](HttpError.png)
        <br>
        After some googling, I realized this was attributed to conda's installer not copying some dll files from the Scripts to the Library\bin folder.
        <br>
        After manually copying them over, I was able to create the environment as such:
        <br>
          
        ![image](CondaEnvSuccess.png)<br/>
     </br>
    2. Installing a package
    - I installed pyauto gui into the environment with no trouble:

        ![image](Package.png)  <br>
    3. Generate requirements.txt file   
            
    - Used the command to generate my file with all the necessary packages:
                
            pip freeze requirements.txt

    
    


