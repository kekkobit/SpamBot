import botogram
bot = botogram.create("YOUR API KEY")
bot.owner = "BOT OWNER"

@bot.command("spam")
def spam_command(chat, message, args):
    """Spam For big Groups!
    This command send the word "spam"
    """ 
    for i in range (Number):
        chat.send("*SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM SPAM*")
       

if __name__ == "__main__":
    bot.run()

