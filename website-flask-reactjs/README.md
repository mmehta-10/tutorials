## Source: https://developer.okta.com/blog/2018/12/20/crud-app-with-python-flask-react

```
$ pipenv install flask==1.0.2

Creating a virtualenv for this project…
Pipfile: /home/meghamehta/scratch/tutorials/website-flask-reactjs/kudos_oss/Pipfile
Using /usr/bin/python3 (3.6.8) to create virtualenv…
⠸ Creating virtual environment...created virtual environment CPython3.6.8.final.0-64 in 830ms
  creator CPython3Posix(dest=/home/meghamehta/.local/share/virtualenvs/kudos_oss-53D7gS07, clear=False, global=False)
  seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=/home/CIQDEV/meghamehta/.local/share/virtualenv)
    added seed packages: pip==20.1.1, setuptools==49.2.0, wheel==0.34.2
  activators BashActivator,CShellActivator,FishActivator,PowerShellActivator,PythonActivator,XonshActivator

✔ Successfully created virtual environment!
Virtualenv location: /home/meghamehta/.local/share/virtualenvs/kudos_oss-53D7gS07
Creating a Pipfile for this project…
Installing flask==1.0.2…
Adding flask to Pipfile's [packages]…
✔ Installation Succeeded
Pipfile.lock not found, creating…
Locking [dev-packages] dependencies…
Locking [packages] dependencies…
Building requirements...
Resolving dependencies...
✔ Success!
Updated Pipfile.lock (b89d92)!
Installing dependencies from Pipfile.lock (b89d92)…
  ���   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 0/0 — 00:00:00
To activate this project's virtualenv, run pipenv shell.
Alternatively, run a command inside the virtualenv with pipenv run.

### For reactjs, install yarn
```

```
# source:
# https://linuxize.com/post/how-to-install-yarn-on-centos-7/

# If you already don’t have Node.js installed on your system, enable the Nodesource repository with the following curl command :
cd /tmp
curl --silent --location https://rpm.nodesource.com/setup_10.x | sudo bash -
sudo yum install -y nodejs

# To enable the Yarn repository and import the repository’s GPG key issue the following commands:
curl --silent --location https://dl.yarnpkg.com/rpm/yarn.repo | sudo tee /etc/yum.repos.d/yarn.repo
sudo rpm --import https://dl.yarnpkg.com/rpm/pubkey.gpg
sudo yum install -y yarn
```
