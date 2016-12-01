from PIL import Image, ImageFont, ImageDraw

import tweets

tweets = tweets.get_tweets()

for i, tweet in enumerate(tweets):

    base = Image.open("boat.jpg").convert('RGBA')
    fnt = ImageFont.truetype('Impact.ttf', 30)
    txt = Image.new('RGBA', base.size, (255, 255, 255, 0))

    d = ImageDraw.Draw(txt)
    d.text((10, 60), tweet, font=fnt, fill=(255, 255, 255, 255))

    out = Image.alpha_composite(base, txt)
    out.save('output/{}'.format(i), 'JPEG')
