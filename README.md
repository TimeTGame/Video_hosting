# Video hosting website template in Django

## Requirements

[Git](https://git-scm.com/downloads)
[Python](https://www.python.org/downloads/): 3.10, 3.11, 3.12, 3.13

## Installation

Clone the repository:

```shell
git clone https://github.com/TimeTGame/Video_hosting.git
cd Video_hosting
```

### Installation on Mac and Linux

At this point, you can install dependencies for prod, test, and dev modes.
Example for prod mode:

```shell
python3 -m venv .venv
source venv/bin/activate
python3 -m pip install -r ./requirements/prod.txt
```

To run in other modes, use dev.txt and test.txt

### Installation on Windows

At this point, you can install dependencies for prod, test, and dev modes.
Example for prod mode:

```shell
python -m venv .venv

# Windows (PowerShell)
.\venv\Scripts\Activate.ps1

# Windows (cmd.exe)
.\venv\Scripts\activate.bat

python -m pip install -r ./requirements/prod.txt
```

To run in other modes, use dev.txt and test.txt

## Run

Go to the project directory:

```shell
cd video_hosting
```

Copy the template.env file and rename it to .env:

```shell
cp template.env .env
```

Starting the server:

```shell
# Windows
python manage.py migrate
python manage.py runserver

# Mac и linux
python3 manage.py migrate
python3 manage.py runserver
```

The test server is hosted at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Setup

Settings are configured through the video_hosting/.env file.
