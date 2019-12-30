FROM python:3.7

WORKDIR /app

# Update package versions
RUN apt-get update

# Insall gettext for i18n
RUN apt-get install -y gettext libgettextpo-dev

# Firstly, copy requirements file
COPY requirements.txt /app/requirements.txt

# Install requirement packages
RUN pip install -r requirements.txt

# Copy all project folders
COPY . /app

# Compile .po files
RUN python manage.py compilemessages -l tr
RUN python manage.py compilemessages -l en

EXPOSE 8000
