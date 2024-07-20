import argparse
import requests
import json
from shutil import rmtree
import os

class GitUpdater:
    def __init__(self, fine_grainied_key: str):
        self.fine_grained_key = fine_grainied_key
        self.headers = {
            "Accept" : "application/vnd.github+json",
            "Authorization": "Bearer %s"%self.fine_grained_key,
            "X-GitHub-Api-Version" : "2022-11-28"
        } 
    
    def check_dir_exists(self, dir):
        if os.path.exists(dir):
            return True
        return False


    def download_latest(self, owner, repo, branch):
        def download_file(session: requests.Session, url, file_name):
            file_content = session.get(url).content
            with open(file_name, 'wb') as f:
                f.write(file_content)
        
        def clone_directory(url: str, dir_path: str, path: str | None):
            if not self.check_dir_exists(dir_path): os.mkdir(dir_path)
            if path: url = self.URL + '/' + path
            print(url)
            r = requests.Session()
            r.headers = self.headers
            resp = r.get(url)

            if resp.status_code == 200:
                json_files = json.loads(resp.text)
                for file in json_files:
                    name = file['name']
                    path = file['path']
                    f_type = file['type']
                    print(f'{name} : {f_type}')
                    if f_type == "file":
                        download_url = file['download_url']
                        file_name = self.clone_path + '/' + path
                        print('[+] Downloading ', name)
                        download_file(r, download_url, file_name)
                        print('[+] Download Complete: ', name)
                    elif f_type == "dir":
                        dir_path = self.clone_path + "/" + path
                        clone_directory(url, dir_path, path)
                    else:
                        print('unknown file format')
            else:
                print('error:', resp.text)
            r.close()

                
        self.URL = f"https://api.github.com/repos/{owner}/{repo}/contents"
        self.COMMIT_URL = f"https://api.github.com/repos/{owner}/{repo}/commits/{branch}"
        os.mkdir(repo) if not self.check_dir_exists(repo) else rmtree(repo)
        self.clone_path = repo

        session = requests.Session()
        session.headers = self.headers
        resp = session.get(self.COMMIT_URL)
        json_resp = json.loads(resp.text)


        sha = json_resp["sha"]
        message = json_resp["commit"]["message"]

        with open('.installation_info', 'w') as f:
            f.write(json.dumps({"sha": sha, "message": message}))
        session.close()
        clone_directory(self.URL, repo, path=None)
    
    def get_current_version(self):
        """
            File Expected to excist
            File format: json
            Example:
                # Sha of current commit # Commit message of current commit
                {"sha": "1l23h12g31l2g3", "message": "Initial Commit"}
        """
        with open('.installation_info', 'r') as f:
            content = f.read()
        json_content = json.loads(content)
        return json_content

    def is_latest_commit(self, owner, repo) -> tuple[bool, str]:
        current_version = self.get_current_version()
        curr_sha = current_version['sha']
        URL = "https://api.github.com/repos/%s/%s/commits/master"%(owner, repo)
        r = requests.session()
        r.headers = self.headers
        resp = r.get(URL)
        json_string = resp.text
        json_url = json.loads(json_string)
        latest_sha = json_url["sha"]
        latest_commit_msg = json_url["commit"]["message"]

        print('current_sha', curr_sha, 'latest_sha', latest_sha)

        if curr_sha != latest_sha:
            return (False, latest_commit_msg)
        else:
            return (True, latest_commit_msg)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="GitHub Cloner using only requests and github key")
    parser.add_argument("--githubkey", required = True,help="Your fine grained github token", type=str)
    parser.add_argument("--owner", help="username/owner", required = True,type=str)
    parser.add_argument("--repo", required = True,help="The target repository, it can be private if the key has the appropriate read permission", type=str)
    parser.add_argument("--branch", required = True,help="The branch of the repository Eg: main/master", type=str)
    parser.add_argument("--clone", required = True, help="Clone the repository", action="store_true")
    args = parser.parse_args()

    key = args.githubkey
    owner = args.owner
    repo = args.repo
    branch = args.branch
    git_updater = GitUpdater(fine_grainied_key=key)
    git_updater.download_latest(owner=owner, repo=repo, branch=branch)
