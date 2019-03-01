# python runtime
FROM python:3.6.7

WORKDIR /taskcontrol

COPY . /taskcontrol

RUN pip3 install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 80

CMD [ "python3", "run.py" ]

# docker build --tag=taskcontrol .