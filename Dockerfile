# BrendUserbot T.me/BrendUserbot

FROM brendsup/brenduserbot:latest
RUN git clone https://github.com/Neseograyanpeyserdi/professionaluserbot.git /root/professionaluserbot
WORKDIR /root/professionaluserbot/
RUN pip3 install -r requirements.txt
CMD ["python3", "main.py"]
