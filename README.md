<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

<!-- [![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url] -->

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">YEELO_APP DJANGO API</h3>

  <p align="center">
    E-Learning API
    <br />
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

This small project is about to test how i'm going to handle the necessary prerequises of Yello concepts.

<p align="right">(<a href="#top">back to top</a>)</p>

### Built With

This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.

- [Django](https://www.djangoproject.com/)
- [djangorestframework](https://django-filter.readthedocs.io/en/latest/guide/rest_framework.html)
- [djangorestframework-jwt](https://jpadilla.github.io/django-rest-framework-jwt/)
- [django-jazzmin](https://github.com/farridav/django-jazzmin)
- [django-filter](https://django-filter.readthedocs.io/en/latest/)
- [drf-generators](https://pypi.org/project/drf-generators/)
- [psycopg2-binary](https://pypi.org/project/psycopg2-binary/)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.

#### 1. Install python in function of your system.

For more information about it click link below https://www.python.org/downloads/

#### 2. Create a python environment

The environement setup process depends on your system. Do some research to find out how to do it on OS.

For Ubuntu you can use the following commands

```sh
virtualenv -p python3 env
source env/bin/activate
```

For OS WINDOWS you can use the following commands

```sh
virtualenv -p python3 env
source env/bin/activate
```

### Installation

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

1. Clone the repo
   ```sh
   git clone https://github.com/guissemohamedcherif/yello_educ_app.git
   ```

2. Install required python packages

   ```sh
   pip install -r requirements.txt

   ```

3. Create .env file and copy .env.example contents in .env

   ```sh
   mkdir .env
   ```

4. Create postgres database with command line
   ```sh
   psql postgres (to connect to postgresql)
   create database 'database_name'
   create user 'database_username' with encrypted password 'password_db'
   grant all privileges to database 'database_username' on 'database_name';111
   ```

5. Apply database migrations
   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Run the app
   ```sh
   python manage.py runserver
   ```

The api should now be running at http://127.0.0.1:8000/

<p align="right">(<a href="#top">back to top</a>)</p>


## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->

## Contact

Mohamed Cherif GUISSE - [Linkedin-Profile](https://www.linkedin.com/in/mohamed-cherif-guisse/)

Project Link: [git@github.com:guissemohamedcherif/yello_educ_app.git](git@github.com:guissemohamedcherif/yello_educ_app.git)

<p align="right">(<a href="#top">back to top</a>)</p>
