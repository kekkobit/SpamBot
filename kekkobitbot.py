import botogram
bot = botogram.create("183771577:AAEJRPa3POd3QIiotmEJTc9y4ydFRP08IxQ")
bot.owner = "@Kekkobit"

@bot.command("hello")
def hello_command(chat, message, args):
	"""Say hello world to the world!
	This command send "hello world"
    """
	chat.send("*Hello World!*")

@bot.command("spam")
def spam_command(chat, message, args):
    """Spam For big Groups!
    This command send the word "spam"
    """ 
    for i in range (15):
        chat.send("*SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM*")

@bot.command("killkekko")
def killkekko_command(chat, message, args):
	"""Kill kekko just for fun!
	This command Kill Kekko
	"""
	chat.send("*oh my God! You killed kekko :3 you are a really bad person! Pray for kekko! :c*")


if __name__ == "__main__":
    bot.run()

