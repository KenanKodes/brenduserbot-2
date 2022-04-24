# BrendUserbot T.me/BrendUserbot

# BrendUserbot T.me/BrendUserbot

FROM brendsup/brenduserbot:latest
RUN git clone https://github.com/elcjn/brenduserbot.git /root/brenduserbot
WORKDIR /root/brend/
RUN pip3 install -r requirements.txt
CMD ["python3", "main.py"]
