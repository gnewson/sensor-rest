from registry.gitlab.com/quarkus-asl/quarkus-iot/qiot-sensor-service-base:1-aarch64

RUN git clone https://github.com/gnewson/sensor-rest.git

RUN pip3 install -r requirements.txt
