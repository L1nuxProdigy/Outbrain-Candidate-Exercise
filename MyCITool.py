## Requires to install libraries ##
import git  # from gitpython library #
import docker # from docker sdk #
import requests # library to use curl easily #
import time


###     Git Stuff     ###
## did not incorporate tests to input!!! ##
github_repo_url = "https://github.com/L1nuxProdigy/Outbrain-Candidate-Exercise"     ## input("Enter youre github URL:")
repo_system_path = "/home/ubuntu/repotest"                                          ## input("Enter repo destination path:")   ## requires an empty folder ##
repo = git.Repo.clone_from(github_repo_url, repo_system_path, branch='master')

###     Docker Stuff     ###
container_tag = "tagging_it"
container_name = "cherry-py"
container_object = docker.from_env()
container_object.images.build(path=repo_system_path, tag=container_tag)
container_object.containers.run(image=container_tag, detach="true", name=container_name, ports={8080:9090})
container_object.containers.get(container_name)  ## returns an error if container isnt listed- require a test" ##
time.sleep(1) ## program crashes if the request is lunched right away, maybe there is somthing slicker ##
test_response = requests.get('http://127.0.0.1:9090') ## code can break here and require testing ##
if test_response.status_code == 200:
    print("Service is Successfully Running")
else:
    print("Service is NOT RUNNING, Requires Attention")