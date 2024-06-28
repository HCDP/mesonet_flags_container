FROM python:3.12
LABEL org.opencontainers.image.source="https://github.com/hcdp/mesonet_flags_container"
LABEL org.opencontainers.image.description="Container for triggering mesonet flags."

ARG HCDP_API_TOKEN
ENV HCDP_API_TOKEN=$HCDP_API_TOKEN

RUN mkdir -p /actor
ADD exec.py /actor/exec.py

CMD [ "/bin/bash", "/actor/exec.py" ]