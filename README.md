# Outbrain-Candidate-Exercise
requirements:
- ubuntu OS (was tested on 18.04 in AWS)
- docker
- Python 3 (was tested on 3.6.7)
    - python libraries: (not shipped with 3.6.7 and require installation):
        - git (AKA gitpython)
        - docker
    - python libraries: (shipped with 3.6.7 but are mentioned anyhow)
        - requests
        - time
        - os
        - sys


In this Repository you can find the MyCITool python script which accepts a github URL as a parameter and does all the rest


Usage Example: (with this repository)

MyCITool.py https://github.com/L1nuxProdigy/Outbrain-Candidate-Exercise


the program if succeeded will:
- clone the given repository to the "cloned_repo_folder" in the current running location
- will create and run a docker container from the Dockerfile in the given repository at the background with port mapping of 9090:8080 (outside:inside) named cherry-py
- will add the Watcher job located in the given repository as a cronjob
    - Watcher logs will be at /var/log/watcher_log_file
- Successful output will be on screen at the end


This Repository Holds:
- Notes directory, for my own notes- not relevant
- Dockerfile, for the python script to use and run the container with the cherryPy application
- MyCITool.py, the python script
- Watcher, the bash script
- cherry_hello_world.py, basic cherryPy application
            