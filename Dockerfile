FROM django:1.10-python2
ADD . /app
WORKDIR /app
RUN pip install -r requirement.txt
CMD sh -c "python manage.py runserver 0.0.0.0:80"
