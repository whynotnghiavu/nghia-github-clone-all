import os
import subprocess
import requests


def get_github_repos(username):
    repos = []
    page = 1
    while True:
        url = f'https://api.github.com/users/{username}/repos?page={page}&per_page=100'
        response = requests.get(url)
        if response.status_code != 200:
            return None
        page_repos = response.json()
        if not page_repos:
            break
        repos.extend([repo['name'] for repo in page_repos])
        page += 1
    return repos


def github_clone_single(username, name_repo):
    ssh_link = f"git@github.com:{username}/{name_repo}.git"
    owner_dir = os.path.expanduser(f'~/Downloads/Nghia/Git/{username}')
    repo_dir = os.path.join(owner_dir, name_repo)

    if not os.path.isdir(owner_dir):
        os.mkdir(owner_dir)

    os.chdir(owner_dir)

    print(f"🚀 \033[32m{repo_dir}\033[0m")

    if os.path.isdir(repo_dir):
        # print(f"{repo_dir} already exists.")
        pass
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

    # print(f"👉 Step: github_clone_all")

    for username in list_username:
        # print(f"🚀username = {username}")
        github_clone_all(username)
