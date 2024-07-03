FROM python:3.12
LABEL org.opencontainers.image.source="https://github.com/hcdp/mesonet_flags_container"
LABEL org.opencontainers.image.description="Container for triggering mesonet flags."

RUN python -m pip install requests

RUN mkdir -p /actor
ADD exec.py /actor/exec.py

CMD [ "python", "/actor/exec.py" ]