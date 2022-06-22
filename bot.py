import logging
import os
import sys
import random
import praw
from prawcore.exceptions import PrawcoreException

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler(sys.stdout))

PATRICK_LIST = ["patrick", "paddy", "palace", "french", "france", "senegal", "invincible", "captain", "juventus"]
FABIO_LIST = ["fabio", "fábio", "porto", "portugal", "portuguese", "primeira"]
WORDLISTS = [PATRICK_LIST, FABIO_LIST]

class Bot:
    def __init__(self):
        self.reddit = praw.Reddit(
            client_id=os.environ.get('CLIENT_ID'),
            client_secret=os.environ.get('CLIENT_SECRET'),
            username=os.environ.get('REDDIT_USERNAME'),
            password=os.environ.get('REDDIT_PASSWORD'),
            user_agent="<it's Vieira!>"
        )
        self.subreddit = self.reddit.subreddit('Gunners')
        self.search_phrase = 'viera'
        self.comment_ids = set()

    def determineVieira(self, comment):
        comment_counts = [sum([comment.body.lower().count(word) for word in wordlist]) for wordlist in WORDLISTS]
        if comment_counts[0] > comment_counts[1]:
            return "Senegal"
        elif comment_counts[1] > comment_counts[0]:
            return "Portugal"
        else:
            post_text = comment.submission.title + " " + comment.submission.selftext
            post_counts = [sum([post_text.lower().count(word) for word in wordlist]) for wordlist in WORDLISTS]
            if post_counts[0] > post_counts[1]:
                return "Senegal"
            elif post_counts[1] > post_counts[0]:
                return "Portugal"
            else:
                return ["Senegal", "Portugal"][random.randint(0,1)]
            

    def run(self):
        try:
            for comment in self.subreddit.stream.comments(skip_existing=False):
                if self.search_phrase in comment.body.lower() and comment.id not in self.comment_ids and comment.author.name != "VieiraBot":
                    try:
                        print(comment.author)
                        self.comment_ids.add(comment.id)
                        replyStr = f'\n\n*He comes from {self.determineVieira(comment)}, He plays for Arsenal, ~~Viera~~ Ohh, __Vieira__ Ohh!*'
                        replyStr += "\n___\n^(_i'm a bot, dm [my creator](https://www.reddit.com/user/CuriousCurry8) for feedback!_)"
                        print(comment.body.lower())
                        print(replyStr)
                        comment.reply(body=replyStr)
                        logger.info('Replied')
                    except PrawcoreException:
                        logger.exception('Prawcore Exception')
                    except KeyboardInterrupt:
                        logger.exception('Keyboard Interrupt')
        except PrawcoreException:
            logger.exception('Prawcore Exception')

    def test(self):
        for submission in self.subreddit.hot(limit=20):
            for comment in submission.comments:
                if hasattr(comment, "body") and self.search_phrase in comment.body.lower() and comment.id not in self.comment_ids:
                    print(comment.body.lower())
                    print(comment.author.name)
                    print(self.determineVieira(comment))
                    print("*******")




def main():
    bot = Bot()
    # while True:
    #    bot.run()
    bot.run()


if __name__ == '__main__':
    main()