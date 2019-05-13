import git  # from gitpython library #
import docker # from docker sdk #
import requests # library to use curl easily #
import time
import os
import sys

###     Git Stuff     ###
## did not incorporate tests to input!!! ##
github_repo_url = "https://github.com/L1nuxProdigy/Outbrain-Candidate-Exercise"     ## input("Enter youre github URL:")
project_path = os.getcwd()+"/cloned_repo_folder"                                        ## input("Enter repo destination path:")   ## requires an empty folder ##
repo = git.Repo.clone_from(github_repo_url, project_path, branch='master')

###     Docker Stuff     ###
container_tag = "tagging_it"
container_name = "cherry-py"
docker_client = docker.from_env()
docker_client.images.build(path=project_path, tag=container_tag)
docker_client.containers.run(image=container_tag, detach="true", name=container_name, ports={8080:9090})
container = docker_client.containers.get(container_name)

for i in range(10):
    print(f'attempt {i+1}')
    try:
        if container.status == "running":
            api_response = requests.get('http://127.0.0.1:9090')
            if api_response.status_code == 200:
                print("Service is Successfully Running")
                text_to_crontab = "*/1 * * * *   root    "+project_path+"/Watcher"
                f = open("/etc/crontab", "a")
                f.write(text_to_crontab)
                f.close
                break
            else:
                print("Service is NOT RUNNING, Requires Attention")
        time.sleep(1)
        container = docker_client.containers.get(container_name)
    except Exception as err:
        print(f'Somthing went Wrong {err}')
        time.sleep(1)
        continue