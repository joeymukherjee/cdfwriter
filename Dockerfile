FROM python:3-alpine 

RUN apk update && apk add github-cli bash ca-certificates gnupg && rm -rf /var/cache/apk/*

RUN pip3 install twine build

ADD . "/cdfwriter"

WORKDIR "/cdfwriter"

ENTRYPOINT ["/bin/bash"]
