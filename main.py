import financialNews
import smtplib, ssl

news = []  # Put your desired stock news here. For example: ["Tesla", "Amazon"]

def run():
    newsInstance = financialNews.News(news)
    email = financialNews.Email(newsInstance.getNews(), news)
    return email.makeEmail()

run()