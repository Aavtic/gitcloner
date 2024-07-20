# gitcloner


Clone github repositories without using git client only using requests!. We make use of GitHubs API. If you want to clone a private github repository you will need to have a key i.e. GitHub Fine Grained token.
Here is the reference: 
https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-fine-grained-personal-access-token


### Usage
```
python3 gitcloner.py --githubkey <your key> --owner <username> --repo <target repository> --branch <branch> --clone
```