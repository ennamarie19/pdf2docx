# Build Stage
FROM bcapuano/atheris:2.1.1-python3.10
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y libgl-dev libglib2.0-0
ADD . /src
WORKDIR /src
RUN python3 -m pip install .

CMD ["/src/mayhem/fuzz_cal.py"]
