# python_basicFlaskSite
A basic flask app deployed to heroku
<br><br>
![python_basicFlaskSite](demo/demo.gif)
<br><br>
<br><br>
## For Mac:
### To create a virtual environment for app:<br>
run in terminal `python3 -m venv virtual` in a folder containg the folder that has all files in repository. <br><br>
To run python from that virtual env `virtual/bin/python3 <SCRIPT-NAME>`<br><br>
To install flask in env `virtual/bin/pip3 install flask`<br><br>
To run it `virtual/bin/python3 <SCRIPT-NAME>`<br><br>
<br>
### When trying to run locally on localhost:5000 and there is already an app runnin on that port: <br>
To find running ports: <br>
`sudo lsof -i :5000` <br><br>
To kill it <br>
`kill -9 <pid>` <br>
<br>
### To deply to heroku:<br>
First login to heroku `heroku login` <br><br>
Create a heroku app with a unique name `heroku create <APP-NAME>` <br><br>
To view all your apps on heroku `heroku apps`<br><br>
To see all dependecies `virtual/bin/pip3 freeze`<br><br>
To install gunicorn in env `virtual/bin/pip3 install gunicorn` <br><br>
To create requirements file for heroku `virtual/bin/pip3 freeze > requirements.txt` <br><br>
Ensurer "requirements.txt" file is in Demo folder <br><br>
Create a file called "Procfile" wiithout an extension type in Demo folder <br><br>
Into the "Procfile" file write and save "web: gunicorn basicFlask:app" <br><br>
Create a file called "runtime.txt" and in it write and save "python-3.9.5" or other supported runtime versions <br><br>
`git init`<br>
`git add .`<br>
`git commit -m "first commit`<br><br>
To point to app to push <br>
`heroku git:remote -a <APP-NAME>`<br><br>
To push it to heroku <br>
`git push heroku master`<br>
<br>
#### To push updates:
Make sure you are pointing to the right app<br>
`heroku apps`<br>
`heroku info`<br>
`git add .`<br>
`git commit -m "second commit"`<br>
`heroku git:remote -a <APP-NAME>`<br>
`git push heroku master`<br>
