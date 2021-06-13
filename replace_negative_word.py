#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 22:13:53 2020

@author: ayyoub
"""

text = """
How many times have you lied down on your bed planning to relax while watching a television show/film, or to read a new book/magazine, only to find out that your dormitory lamp was not sufficiently serving your lighting needs? If the answer is more than once, then it is presumably time to go lamp shopping.

 With a vast variety of lamps to choose from, getting the perfect lamp is actually a matter of having the needed time and energy to spend in an effort to locate it. Since lighting is very crucial to the function and looks of a room, with the numerous lamp options available currently on the market, finding your next lamp can become a bit overwhelming-especially if you have to decide on what can cover your present lighting needs. It can in fact be a rather time-consuming endeavor trying to select among a wall lamp, a candle lamp, a feng shui lamp, a floor lamp, an antler lamp, a contemporary lamp, or an accent lamp. This is why it is important to follow some essential guidelines.

 Given that you know the area you wish to add that extra bit of lighting, begin by calculating out the exact location you need to place your new lamp prior to obtaining it. Is it best for it to be placed on a table, to be hanged from a wall, or to securely stand on the room's floor? Upon concluding on this decision, you can clearly move on to the next one, which is selecting a basic lamp size. Offered in different shapes and heights, lamps can be offer anything from usual to very particular lighting. If you need a lamp that offers general lighting go for taller samples, while if you want to succeed in producing a more romantic atmosphere, select a smaller one that its shade does not allow a lot of lighting beams to escape.

That brings you to the bulb decision. If you need to have affluent lighting available anytime you turn on your lamp, then it is better if you select to buy a halogen type of bulb, which has a much lighter and whiter ray. Incandescent bulbs provide a softer and somewhat yellowier hue that is not proper if you intend to read while using the lamp. But, these types of bulbs are perfect if you want to achieve soft, careful lighting that does not attract too much your eye's attention. Given the above, it is probably time to decide on whether your new lamp will be used also for ornamental or clearly functional purposes. If you wish to backlight your cabinet, then placing an accent lamp on top is a much better alternative than a floor lamp, which can be used if you wish to toe light your favorite piece of floor-art.

 Finally, the height of your shade should match the height of your lamp from the base to the socket. Even if you decide not to follow this usual rule, make sure the final result looks proportionately right. Be sure to choose a lamp style that is equivalent to your room and to follow its theme. Your lamp's or its shade's color has to match the rest of the room's furniture, fabrics, and accessories. Carefully select your lamp's colors as these will be displayed at all times.
"""

negative = ['is not', 'Is not',
            'are not', 'Are not',
            'was not', 'Was not',
            'were not', 'Were not',
            'do not', 'Do not',
            'does not', 'Does not',
            'did not', 'Did not',
            'can not', 'Can not',
            'could not', 'Could not',
            'should not', 'Should not',
            'would not ', 'Would not ',
            'will not', 'Will not',
            'shall not', 'Shall not',
            'it is', 'It is' 
            ]

replace_with = ["isn't", "Isn't",
                "aren't", "Aren't",
                "wasn't", "Wasn't",
                "weren't", "Weren't",
                "don't", "Don't",
                "doesn't", "Doesn't",
                "didn't", "Didn't",
                "can't", "Can't",
                "couldn't", "Couldn't",
                "shouldn't", "Shouldn't",
                "wouldn't", "Wouldn't",
                "won't", "Won't",
                "shan't", "Shan't",
                "it's", "It's"
                ]

found = []
     
for i in range(0, len(negative)):
    if text.find(negative[i]) != -1:
        print(negative[i])
        found.append(negative[i])
        text = text.replace(negative[i],replace_with[i])