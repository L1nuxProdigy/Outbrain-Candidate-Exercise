FROM python:3.7
RUN pip3 install cherryPy
COPY cherry_hello_world.py cherry_hello_world.py
ENTRYPOINT ["python3", "cherry_hello_world.py"]