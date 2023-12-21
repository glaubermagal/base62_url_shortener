# Blue Coding Challenge Documentation

Welcome to the Blue Coding Challenge documentation! This URL shortener is built using Python, Django, and PostgreSQL, with an additional Celery worker for fetching the title of input URLs and storing it in the database.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Running the Project](#running-the-project)
- [Testing](#testing)
- [Usage](#usage)
- [Shortening Algorithm](#shortening-algorithm)

## Requirements

Make sure you have the following tools installed:

- Docker
- Docker Compose

## Installation

Clone the repository:

```bash
git clone git@github.com:glaubermagal/blue_coding_test.git
cd blue_coding_test
```

Create a local_settings.py file in django_project folder with the following content:

```python
BASE_URL = 'http://localhost:8000'
```


## Running the Project

Use Docker Compose to start the project:

```bash
docker-compose up
```

## Testing

While the project is running, open another terminal and access the server container:

```bash
docker-compose exec server bash
```

Then, run the tests:

```bash
python manage.py test apps/*
```

## Usage

1. **List of the Top 100 Most Visited URLs in descending order:**
   ```bash
   curl http://localhost:8000/list/
   ```

Example output:

```json
[
    {
        "long_url": "https://agilemanifesto.org/",
        "short_url": "http://localhost:8000/y",
        "title": "Manifesto for Agile Software Development"
    },
    {
        "long_url": "https://cloud.google.com/duet-ai?hl=en",
        "short_url": "http://localhost:8000/z",
        "title": "Duet AI for Developers"
    },
    {
        "long_url": "https://docs.python.org/3/tutorial/modules.html",
        "short_url": "http://localhost:8000/10",
        "title": "6. Modules — Python 3.12.1 documentation"
    },
    {
        "long_url": "https://cloud.google.com/code/docs/vscode/auth_success",
        "short_url": "http://localhost:8000/11",
        "title": "Cloud Code for VS Code is now authorized to access your account  |  Google Cloud"
    },
    {
        "long_url": "https://accounts.binance.com/en/register",
        "short_url": "http://localhost:8000/12",
        "title": "Bitcoin Exchange | Cryptocurrency Exchange | Binance"
    },
    {
        "long_url": "https://jsonformatter.org/",
        "short_url": "http://localhost:8000/13",
        "title": "Best JSON Formatter and JSON Validator: Online JSON Formatter"
    }
]
```

2. **Shorten a URL:**
   ```bash
   curl http://localhost:8000/shorten/?url=<long_url>
   ```

```json
{
    "short_url": "http://localhost:8000/y"
}
```

3. **Redirect to the Original URL:**
   ```bash
   curl http://localhost:8000/<base62_id>/
   ```

4. **Managing the list of URLs registered in the database:**

Create a super user

```bash
docker-compose exec server bash
python manage.py createsuperuser
```

Access the admin panel and insert your credentials:

```bash
http://localhost:8000/admin/
```

## Shortening Algorithm

The [shortening algorithm](/apps/urls/utils.py) is based on the [base62](https://en.wikipedia.org/wiki/Base62) numeric system. It utilizes the auto-incremented ID field of the URLs table as input to convert the numeric base, achieving the shortest possible length of a unique ID that can be used in a URL.

Feel free to explore the code and contribute to the improvement of this project. If you encounter any issues or have suggestions, please open an issue on the [GitHub repository](https://github.com/glaubermagal/blue_coding_test).