# Terminal Command

### Django Requires Python

To check if your system has Python installed, run this command in the command prompt:

    python --version

### PIP

To check if your system has PIP installed, run this command in the command prompt:

    pip --version

### Virtual Environment

- Windows:

        py -m venv myworld

- Unix/MacOS:

        python -m venv myworld

Then you have to activate the environment, by typing this command:

- Windows:

        myworld\Scripts\activate.bat

- Unix/MacOS:

        source myworld/bin/activate

### Install Django

- Windows:

        py -m pip install Django

- Unix/MacOS:

        python -m pip install Django

### Windows, Mac, or Unix?

You can run this project on either one. There are some small differences, like when writing commands in the command prompt, Windows uses ==py== as the first word in the command line, while Unix and MacOS use ==python==:

- Windows:

        py --version

- Unix/MacOS:

        python --version

### Check Django Version

You can check if Django is installed by asking for its version number like this:

    django-admin --version

# Django Create Project

My First Project
Once you have come up with a suitable name for your Django project, like mine: ==my_tennis_club==, navigate to where in the file system you want to store the code (in the virtual environment), I will navigate to the ==myworld== folder, and run this command in the command prompt:

    django-admin startproject my_tennis_club

### Run the Django Project

Now that you have a Django project, you can run it, and see what it looks like in a browser.

Navigate to the /my_tennis_club folder and execute this command in the command prompt:

    py manage.py runserver

### Create App

I will name my app members.

Start by navigating to the selected location where you want to store the app, in my case the ==my_tennis_club== folder, and run the command below.

If the server is still running, and you are not able to write commands, press ==[CTRL] [BREAK]==, or ==[CTRL] [C]== to stop the server and you should be back in the virtual environment.

    py manage.py startapp members

### Django URLs

If the server is not running, navigate to the /my_tennis_club folder and execute this command in the command prompt:

    py manage.py runserver

### Change Settings

To be able to work with more complicated stuff than "Hello World!", We have to tell Django that a new app is created.

This is done in the settings.py file in the my_tennis_club folder.

Look up the INSTALLED_APPS[] list and add the members app like this:

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'members'
    ]

Then run this command:

    py manage.py migrate

Start the server by navigating to the /my_tennis_club folder and execute this command:

    py manage.py runserver

# Django Models

### Create Table (Model)

To create a model, navigate to the models.py file in the /members/ folder.

Open it, and add a Member table by creating a Member class, and describe the table fields in it:

- my_tennis_club/members/models.py:

        from django.db import models

        class Member(models.Model):
            firstname = models.CharField(max_length=255)
            lastname = models.CharField(max_length=255)

### Migrate

Now when we have described a Model in the models.py file, we must run a command to actually create the table in the database.

Navigate to the /my_tennis_club/ folder and run this command:

    py manage.py makemigrations members

Note that Django inserts an id field for your tables, which is an auto increment number (first record gets the value 1, the second record 2 etc.), this is the default behavior of Django, you can override it by describing your own id field.

The table is not created yet, you will have to run one more command, then Django will create and execute an SQL statement, based on the content of the new file in the /migrations/ folder.

Run the migrate command:

    py manage.py migrate

### View SQL

As a side-note: you can view the SQL statement that were executed from the migration above. All you have to do is to run this command, with the migration number:

    py manage.py sqlmigrate members 0001

# Django Insert Data

### Add Records

The Members table created in the previous chapter is empty.

We will use the Python interpreter (Python shell) to add some members to it.

To open a Python shell, type this command:

    py manage.py shell

At the bottom, after the three >>> write the following:

    from members.models import Member

Hit [enter] and write this to look at the empty Member table:

    Member.objects.all()

This should give you an empty QuerySet object, like this:

    <QuerySet []>

Add a record to the table, by executing these two lines:

    member = Member(firstname='Emil', lastname='Refsnes')
    member.save()

Execute this command to see if the Member table got a member:

    Member.objects.all().values()

Hopefully, the result will look like this:

    <QuerySet [{'id': 1, 'firstname': 'Emil', 'lastname': 'Refsnes'}]>

### Add Multiple Records

You can add multiple records by making a list of Member objects, and execute .save() on each entry:

    member1 = Member(firstname='Tobias', lastname='Refsnes')
    member2 = Member(firstname='Linus', lastname='Refsnes')
    member3 = Member(firstname='Lene', lastname='Refsnes')
    member4 = Member(firstname='Stale', lastname='Refsnes')
    member5 = Member(firstname='Jane', lastname='Doe')
    members_list = [member1, member2, member3, member4, member5]
    for x in members_list:
      x.save()

Now there are 6 members in the Member table:

    Member.objects.all().values()
    <QuerySet [{'id': 1, 'firstname': 'Emil', 'lastname': 'Refsnes'},
    {'id': 2, 'firstname': 'Tobias', 'lastname': 'Refsnes'},
    {'id': 3, 'firstname': 'Linus', 'lastname': 'Refsnes'},
    {'id': 4, 'firstname': 'Lene', 'lastname': 'Refsnes'},
    {'id': 5, 'firstname': 'Stale', 'lastname': 'Refsnes'},
    {'id': 6, 'firstname': 'Jane', 'lastname': 'Doe'}]>
