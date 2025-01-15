# RPA Get Started

This project demonstrates how to run RPA (Robotic Process Automation) scripts.

## Prerequisites

- Python 3.8 or higher
- Poetry (Python package manager)
  ```bash
  pipx install poetry
  ```
- Git

## Installation

1. Clone the repository:

```bash
git clone git@github.com:FALAK097/rpa_get_started.git
cd rpa_get_started
```

2. Set up Python environment:

```bash
poetry shell
poetry install
```

## Configuration

1. Open `config.json` and update with your credentials:

```json
{
  "LOGIN_URL": "https://outriskai.com/login",
  "USERNAME": "your_username",
  "PASSWORD": "your_password"
}
```

## Running the Project

Execute the RPA script by running:

```bash
./rpa_run.sh
```

## Notes

- Make sure to keep your credentials secure and never commit them to version control
- If you encounter permission issues with `rpa_run.sh`, run: `chmod +x rpa_run.sh`
