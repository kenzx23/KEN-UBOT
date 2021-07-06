# KEN UBOT
FROM koala21/kampangbot:buster

#
# KEN
#
RUN git clone -b KEN-UBOT https://github.com/kenzx23/KEN-UBOT /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/kenzx23/KEN-UBOT/KEN-UBOT/requirements.txt

CMD ["python3","-m","userbot"]
