FROM python:3.7

WORKDIR /app

# Update package versions
RUN apt-get update

# Insall gettext for i18n
RUN apt-get install -y gettext libgettextpo-dev

# Firstly, copy requirements file
COPY ./requirements.txt ./requirements.txt

# Install requirement packages
RUN pip install -r requirements.txt

# copy docker-entrypoint.sh
COPY ./docker-entrypoint.sh ./docker-entrypoint.sh

# Copy all project folders
COPY . .

# run docker-entrypoint.sh
ENTRYPOINT ["./docker-entrypoint.sh"]

# Expose port
EXPOSE 8000
