import random

from tiktokautouploader import upload_tiktok


DESCRIPTIONS = [
    "The latest season of Family Guy is here, so lets take a look back at some of the funniest and most memorable moments from previous seasons.",
    "Taking a look back at some of the funniest Family Guy moments.",
    "Some of the most memorable Family Guy moments all in one place.",
    "Family Guy has given us some absolutely ridiculous moments. Here are a few.",
    "A quick look back at some classic Family Guy moments.",
    "Here are some of the funniest moments Family Guy has given us over the years.",
    "Looking back at some unforgettable Family Guy moments.",
    "Some classic Family Guy moments that never get old.",
    "Family Guy has had some seriously hilarious moments. Here are some of the best.",
    "A collection of some of the funniest moments from Family Guy.",
    "Remember these Family Guy moments? Here's a quick trip down memory lane.",
    "Some Family Guy moments that still hit just as hard today.",
    "Taking another look at some classic moments from Family Guy.",
    "Family Guy never seems to run out of ridiculous moments.",
    "A few of the funniest and most memorable moments from Family Guy.",
    "Here are some classic Family Guy moments worth watching again.",
    "Some of the funniest Family Guy scenes from previous seasons.",
    "Looking back at some moments that made Family Guy so memorable.",
    "Family Guy has produced some legendary comedy over the years.",
    "A quick compilation of some unforgettable Family Guy moments.",
    "Some hilarious Family Guy moments you might remember.",
    "Going back through some of the funniest moments from Family Guy.",
    "These Family Guy moments are still hilarious after all these years.",
    "A few classic Family Guy moments for anyone who needs a laugh.",
    "Some of the most ridiculous moments we've seen on Family Guy.",
    "Family Guy has no shortage of hilarious moments. Here are a few.",
    "Let's take a look at some classic Family Guy comedy.",
    "A collection of funny and memorable moments from Family Guy.",
    "Revisiting some of the funniest scenes from Family Guy.",
    "Just a few classic Family Guy moments to bring back some memories.",
]

def get_description():
    return random.choice(DESCRIPTIONS)


def upload_video(video):

    upload_tiktok(
        video=video,
        description=get_description(),
        accountname='garmonto6',
        hashtags=[
            '#usa',
            '#familyguy',
            '#comedy',
            '#fyp',
            '#funny'
        ],
        copyrightcheck=True,
        suppressprint=False
    )