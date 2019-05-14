import git  # from gitpython library #
import docker # from docker sdk #
import requests # library to use curl easily #
import time
import os
import sys

def clone_git_repo(github_repo_url, project_path):
	git.Repo.clone_from(github_repo_url, project_path, branch='master')
	
def create_container(container_tag, container_name, project_path):
	docker_client = docker.from_env()
	docker_client.images.build(path=project_path, tag=container_tag)
	docker_client.containers.run(image=container_tag, detach="true", name=container_name, ports={8080:9090})
	
def add_watcher_cronjob(project_path):
	text_to_crontab = "*/1 * * * *   root    "+project_path+"/Watcher\n"
	f = open("/etc/crontab", "a")
	f.write(text_to_crontab)
	f.close

def main():
	## Git Part ##
	github_repo_url = sys.argv[1]
	project_path = os.getcwd()+"/cloned_repo_folder"
	clone_git_repo(github_repo_url,project_path)
	
	## Docker Part ##
	container_tag = "tagging_it"
	container_name = "cherry-py"
	create_container(container_tag, container_name, project_path)
	docker_client = docker.from_env()
	container = docker_client.containers.get(container_name)

	## Main Test ##
		## 10 iterations to check whether the container and service are up ##
		## the number of iterations randomly chosed as a way of a timeout ##
		## if the container and service are up it will ad the watcher cronjob ##
	for i in range(10):
		print(f'attempt {i+1}')
		try:
			if container.status == "running":
				api_response = requests.get('http://127.0.0.1:9090')
				if api_response.status_code == 200:
					print("Service is Successfully Running")
					add_watcher_cronjob()
					break
				else:
					print("Service is NOT RUNNING, Requires Attention")
			time.sleep(1)
			container = docker_client.containers.get(container_name)
		except Exception as err:
			print(f'Somthing went Wrong {err}')
			time.sleep(1)
			continue
			
if __name__ == "__main__":
	main()