from PIL import Image, ImageFont, ImageDraw

import tweets

tweets = tweets.get_tweets()

for i, tweet in enumerate(tweets):

    base = Image.open("boat.jpg").convert('RGBA')
    fnt = ImageFont.truetype('Impact.ttf', 30)
    txt = Image.new('RGBA', base.size, (255, 255, 255, 0))

    # The greatest line wrapping function
    tweetlines = [tweet[:32], tweet[32:64], tweet[64:96], tweet[96:]]

    d = ImageDraw.Draw(txt)
    d.text((10, 32), tweetlines[0], font=fnt, fill=(255, 255, 255, 255))
    d.text((10, 64), tweetlines[1], font=fnt, fill=(255, 255, 255, 255))
    d.text((10, 128), tweetlines[2], font=fnt, fill=(255, 255, 255, 255))
    d.text((10, 256), tweetlines[3], font=fnt, fill=(255, 255, 255, 255))

    out = Image.alpha_composite(base, txt)
    out.save('output/{}'.format(i), 'JPEG')
