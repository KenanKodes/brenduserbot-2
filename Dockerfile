# BrendUserbot T.me/BrendUserbot

FROM elcjn/brenduserbot:latest
RUN git clone https://github.com/elcjn/brenduserbot.git /root/brenduserbot
WORKDIR /root/brenduserbot/
RUN pip3 install -r requirements.txt
CMD ["python3", "main.py"]
