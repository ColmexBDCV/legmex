FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /legmex
WORKDIR /legmex
COPY requirements.txt /legmex/
RUN pip install --trusted-host pypi.org -r requirements.txt
COPY . /legmex/
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]