[![Python Version](https://img.shields.io/badge/python-3.7-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-2.1-brightgreen.svg)](https://djangoproject.com)

# Intern Work 

This contains full working login/SignUp System with forgot your password and after you get logged in you can also upload one photo and see it by clicking Image Tab on Nav Bar.

## Running the Project Locally

First, clone the repository to your local machine:

```bash
git clone https://github.com/9916103020/intern_work2.git
```

Install the requirements:

```bash
pip install -r requirements.txt
```

Apply the migrations:

```bash
python manage.py migrate
```

Collect the Static folder files:

```bash
python manage.py collectstatic
```

Finally, run the development server:

```bash
python manage.py runserver
```

The project will be available at **127.0.0.1:8000**.

## Forgot Your Password Working

When you click on forgot your password link you will be taken to another page where it will be asking for email id you have registered with and then hit sumbit button.

![](Images/Forgot.PNG)

Locally on your cpmmand line you will be given a link which will take you to password reset page.

![](Images/Email.PNG)

Password Reset Page.

![](Images/Reset.PNG)

## Image Saved in Static

When you click on add image button and then click upload image.  

![](Images/Upload%20Button.PNG)

Image will be saved in static folder with your username so that we can easily extract image to show users.

![](Images/Saved.PNG)

For extracting image from static folder using username.

Code:
```bash
<img src ="{% static ''%}{{ user }}.png">
```

Now you can click on Image tab on Nav bar to see your image you uploaded.

![](Images/View.PNG)



