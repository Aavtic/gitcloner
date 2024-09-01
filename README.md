# GitCloner

Clone github repositories without using git!, only using requests!. We make use of GitHubs API. If you want to clone a private github repository you will need to have a key i.e. GitHub Fine Grained token.
Here is the reference:
[fine grained token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-fine-grained-personal-access-token) 

## Effortless Repository Cloning with GitCloner

GitCloner is a Python-based tool that simplifies the process of cloning GitHub repositories, even in environments where Git is not installed. Whether you are working with public or private repositories, GitCloner provides a seamless and secure way to clone repositories using the GitHub API.

## Features

- **No Git Installation Required**: Clone repositories without needing Git installed on your system.
- **Private Repository Access**: Securely clone private repositories using a Fine-Grained GitHub token.
- **User-Friendly**: Designed for users with minimal technical expertise, making repository management simple and accessible.
- **Flexible Cloning**: Supports cloning specific branches and integrates easily into various workflows.

## How It Works

To use GitCloner, simply run the program with the necessary command-line options. Here's an example:

```bash
python3 gitcloner.py --githubkey <your key> --owner <username> --repo <target repository> --branch <branch> --clone
```

# Note
- githubkey: Your Fine-Grained GitHub token (required for private repositories).
- owner: The GitHub username of the repository owner.
- repo: The name of the repository you want to clone.
- branch: The branch of the repository you wish to clone (default is the main branch).
- clone: Initiates the cloning process.

# Installation

Ensure you have Python 3 installed on your system.

Clone this repository and navigate to the project directory.

Install the required dependencies using:

# Usage

After installation, you can use GitCloner to clone repositories by providing the necessary details through the command line. For example:

``` bash
python3 gitcloner.py --githubkey abc123 --owner johndoe --repo myrepo --branch main --clone
```

# Problem Addressed

GitCloner simplifies repository access by eliminating the need for Git installation, making it easy for users in restricted or non-technical environments to clone both public and private repositories securely.
Innovation and Uniqueness

GitCloner uniquely leverages the GitHub API to enable repository cloning without requiring Git on the user's system. This solution combines secure private access with ease of use, making it a valuable tool for a wide range of users.
License

This project is licensed under the MIT License - see the LICENSE file for details.
Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or features you'd like to see.
Contact

For any inquiries or support, please contact aadishmkerala@gmail.com.
