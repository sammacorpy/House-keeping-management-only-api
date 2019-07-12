*APIS for the given functionality*
to run this app

step 1: install python visit link: https://www.python.org/downloads/release/python-374/
step 2: install pip if it does not come with python
step 3: check if pip is installed or not by executing this command `pip --version`

step 4: run `pip install django-admin`
step 5: run `pip install djangorestframework`

step 6: open this project in any terminal 
step 7: get inside HouseKeepingManagementSystem folder
step 8: run `python manage.py makemigrations`
step 9: run `python manage.py migrate`
step 10: run `python manage.py runserver`

after running the server goto this link 1=>  http://localhost:8000/admin/      login with username as 'sam'  & password is 'admin'  this is admin page which contains view of all database.


link 2=> http://localhost:8000/api/v1/auth/login/ visit this link to get logged in    //login with username as 'sam'  & password is 'admin'

link 5=> http://localhost:8000/api/v1/  API list 1 which have all the urls of api end point please visit.

link 6=> http://localhost:8000/api/v1/assigntask/  API list 2 which have  api end-points to assign task and to view all the task assigned to workers  extended version http://localhost:8000/api/v1/assigntask/?worker=2 to get details of worker with id 2 only

I have followed rest frame work 





link 5=> http://localhost:8000/api/v1/auth/logout/ to logout



