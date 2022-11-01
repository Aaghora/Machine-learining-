# Machine-learining-
This is one of Machine learning projects

Creating Conda environment
'''

conda create -p venv python==3.10 -y
'''

conda activate venv
'''
or
'''
conda activate venv/
'''

'''
pip install -r requirements.txt
'''
creating App.py folder
'''
python app.py #to run the app.

'''
git commands
'''

git status -- #To know the status of the work
'''

git add <file name>  -- #to upload files
'''

git add .   -- #to upload all the files
'''

git log  --- #to check the  created versions of the apps (with head point to the current version)
'''

< Note: To ignore a file or folder from  git  we can add the file or folder name in .gitignore folder
'''

git commit -m "message"------ #To create version/ commit all changes by git
''' 

To send versions/ changes to github
'''
git push origin main
'''

To check remote url
'''
git remote -v
'''

To setup CI/CD pipeline in Heroku we basically need 3 information
1. Heroku_Email_ID= *************@gmail.com
2. Heroku_API_Key= ************************
3. Heroku_App_Name= ml-1regression
'''

Build DOCKER IMAGE
'''

docker build -t <image_name>:<tag_name> .      ## (.) for the current location directory
'''
NOTE: Image name of docker should be in lower case
'''
To list docker images
'''
 docker images
 '''
 To Run docker image
 '''
 docker run -p 5000:5000 -e PORT=5000 <image id>
 '''

 TO check running containers in docker
 '''
docker ps
'''

To stop docker container
'''
docker stop <container_id>
'''
Gunicorn command 
'''
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT <module name>:<flask object>
'''

To install all the requirements use
'''
python setup.py install
'''

packages = find_packages()
# will search our code and return all the packages which have __init__ in there names.
'''
install_requires "holds all the external packages needed by us for our use

'''
<-e . library > in absence of it " pip install -r reruirements.txt" will only install the external libraries and not the internal ones with __ init__.py names on updation of the versions
'''
install ipykernel
'''
pip install ipykernel
'''
