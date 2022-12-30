##### building stage #####
FROM --platform=linux/amd64 python:3.10

RUN apt-get update && apt-get install -y \
    unzip \
    wget \
    curl \
    gnupg

# chrome driver
ADD https://chromedriver.storage.googleapis.com/108.0.5359.71/chromedriver_linux64.zip /opt/chrome/
RUN cd /opt/chrome/ && \
    unzip chromedriver_linux64.zip && \
    rm -f chromedriver_linux64.zip

# python package
RUN pip install --upgrade pip
COPY /app/requirements.txt ./
RUN pip install --no-cache-dir -r  requirements.txt

# chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add && \
    echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' | tee /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && \
    apt-get install -y google-chrome-stable && \
    apt-get -y clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app
ENV FLASK_APP=app

ENV PATH /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/opt/chrome
