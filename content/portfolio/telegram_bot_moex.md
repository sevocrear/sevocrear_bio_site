---
title: MOEX Telegram Bot
date: 2020-12-15
thumbnail: images/portfolio/MOEX_bot.png
service: Telegram Bot
client: Vladislav Z.
shortDescription: It was needed to program telegram bot which will take some stock info rom moex.ru, extract it and output to the subscribed users each day at pre-defined time
challenge: Use Python language and TelegramBotAPI so users could use the bot in order to know top 10 volatile stock of the day and their trade volumes.

solution: telebot, matplotlib and pandas libraries were used in order to do create the bot. Also, multithreading was implemented in order to diverge interaction with the user and auto sending stock info to all the users.

---

I decided to use *.npy file in order to store users IDs and max value of the stock they'd like to see in the chat. So, the idea was to constrain the price of the stocks for certain users. After that, MySQL could be implemented.

![Bot](/images/portfolio/bot_MOEX.png)

The example result of the bot output you can see above.


Also, it should be mentioned that the bot could be deployed on the server in order to be fully automated.
