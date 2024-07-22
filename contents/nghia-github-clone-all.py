import os
import subprocess
# pip install requests
import requests


def get_github_repos(username):
    url = f'https://api.github.com/users/{username}/repos'
    response = requests.get(url)
    if response.status_code == 200:
        repos = response.json()
        return [repo['name'] for repo in repos]
    else:
        return None


def github_clone_single(username, name_repo):
    ssh_link = f"git@github.com:{username}/{name_repo}.git"
    owner_dir = os.path.expanduser(f'~/Downloads/Nghia/Git/{username}')
    repo_dir = os.path.join(owner_dir, name_repo)

    if not os.path.isdir(owner_dir):
        os.mkdir(owner_dir)

    os.chdir(owner_dir)
    if os.path.isdir(repo_dir):
        print(f"{repo_dir} already exists.")
    else:
        # SSH clone
        subprocess.run(['git', 'clone', ssh_link])
        print(f"Cloned {name_repo} into {owner_dir}")


def github_clone_all(username):
    github_repos = get_github_repos(username)

    if github_repos:
        for i in range(len(github_repos)):
            github_clone_single(username, github_repos[i])
    else:
        print(f'Not find github_repos')


if __name__ == "__main__":

    list_username = [
        "whynotnghiavu",
        # "company20206205",
        # "20206205",

        # "vvn20206205",
        # "hust20206205",
        # "vuvannghia452002",
    ]

    print(f"👉 Step: github_clone_all")

    for username in list_username:
        print(f"🚀username = {username}")
        github_clone_all(username)
