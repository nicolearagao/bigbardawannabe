# BigBardaWannabe overview

The BigBardaWannabe app is a comprehensive fitness tracking tool designed specifically for powerlifters and strength enthusiasts. It allows you to effortlessly track and analyze your training, diet, personal records, and cardio activities to help you achieve your strength goals.


## Motivation

As both a software engineer and a powerlifter, I know firsthand the dedication and effort required to achieve greatness in both domains. The BigBardaWannabe app was born out of my own desire to become stronger and my belief in the transformative power of powerlifting.

## Features

- Track Your Progress: Easily record and monitor your training sessions, personal records, diet, and cardio activities all in one place.

- Generate Reports: Gain valuable insights into your training effectiveness, adherence levels, and overall progress through reports.

## Dependencies

The Python packages that are required for running bigbardawannabe on a system can be found in the `pyproject.toml` file in the section "tool.poetry.dependencies".

### Installing

bigbardawannabe container image can be created from source. THis repository includes a Dockerfile that contains instructions for the image creation of the server. You must have [Docker installed](https://docs.docker.com/engine/installation/).

1. Clone the repository:
   ```
   git clone git@github.com:nicolearagao/bigbardawannabe.git
   ```

2. Build the Docker image through Docker-compose:
   ```
   docker-compose up -d
   ```
Then open a browser and head to https://localhost:8000
Check for api docs on https://localhost:8000/docs