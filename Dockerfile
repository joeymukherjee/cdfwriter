FROM python:3-alpine 

RUN apk update && apk add github-cli bash ca-certificates gnupg && rm -rf /var/cache/apk/*

RUN pip3 install twine build

RUN git config --global user.email "joey.mukherjee@yahoo.com"
RUN git config --global user.name "Joey Mukherjee"

ADD . "/cdfwriter"

WORKDIR "/cdfwriter"

ENTRYPOINT ["/bin/bash"]
