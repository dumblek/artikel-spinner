#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 21:01:28 2020

@author: ayyoub
"""
import random

text = """
How many times have you lied down on your bed planning to relax while watching a television show/film, or to read a new book/magazine, only to find out that your dormitory lamp wasn't sufficiently serving your lighting needs? If the answer is more than once, then it's presumably time to go lamp shopping.\n \n With a vast variety of lamps to choose from, getting the perfect lamp is actually a matter of having the needed time and energy to spend in an effort to locate it. Since lighting is very crucial to the function and looks of a room, with the numerous lamp options available currently on the market, finding your next lamp can become a bit overwhelming-especially if you have to decide on what can cover your present lighting needs. It can in fact be a rather time-consuming endeavor trying to select among a wall lamp, a candle lamp, a feng shui lamp, a floor lamp, an antler lamp, a contemporary lamp, or an accent lamp. This is why it's important to follow some essential guidelines.\n \n Given that you know the area you wish to add that extra bit of lighting, begin by calculating out the exact location you need to place your new lamp prior to obtaining it. Is it best for it to be placed on a table, to be hanged from a wall, or to securely stand on the room's floor? Upon concluding on this decision, you can clearly move on to the next one, which is selecting a basic lamp size. Offered in different shapes and heights, lamps can be offer anything from usual to very particular lighting. If you need a lamp that offers general lighting go for taller samples, while if you want to succeed in producing a more romantic atmosphere, select a smaller one that its shade doesn't allow a lot of lighting beams to escape.\n\nThat brings you to the bulb decision. If you need to have affluent lighting available anytime you turn on your lamp, then it's better if you select to buy a halogen type of bulb, which has a much lighter and whiter ray. Incandescent bulbs provide a softer and somewhat yellowier hue that isn't proper if you intend to read while using the lamp. But, these types of bulbs are perfect if you want to achieve soft, careful lighting that doesn't attract too much your eye's attention. Given the above, it's probably time to decide on whether your new lamp will be used also for ornamental or clearly functional purposes. If you wish to backlight your cabinet, then placing an accent lamp on top is a much better alternative than a floor lamp, which can be used if you wish to toe light your favorite piece of floor-art.\n \n Finally, the height of your shade should match the height of your lamp from the base to the socket. Even if you decide not to follow this usual rule, make sure the final result looks proportionately right. Be sure to choose a lamp style that is equivalent to your room and to follow its theme. Your lamp's or its shade's color has to match the rest of the room's furniture, fabrics, and accessories. Carefully select your lamp's colors as these will be displayed at all times.
"""

list_replace = ["'",'“',"-","_","(",")","{","}","[","]",'<','>',"/","\\",'%','@','²','³','¼','½','¾',":"]
found = []

a = ['&#x00027;','&#39;','&#x00060;','&#96;','&#x000B4;','&#180;','&#x02018;','&#8216;','&#x02019;','&#8217;','&#x02035;','&#8245;','&#x02032;','&#8242;']
b = ['&#x00022;','&#34;','&#x002DD;','&#733;','&#x0201C;','&#8220;','&#x0201D;','&#8221;','&#x02033;','&#8243;']
c = ['&#x02010;','&#8208;','&#x02013;','&#8211;','&#x02014;','&#8212;','&#x02043;','&#8259;']
d = ['&#x0005F;','&#95;','&#x00332;','&#818;']
e = ['&#x00028;','&#40;','&#x02772;','&#10098;','&#x02985;','&#10629;']
f = ['&#x00029;','&#41;','&#x02773;','&#10099;','&#x02986;','&#10630;']
g = ['&#x0007B;','&#123;']
h = ['&#x0007D;','&#125;']
j = ['&#x0005B;','&#91;','&#x027E6;','&#10214;']
k = ['&#x0005D;','&#93;','&#x027E7;','&#10215;']
l = ['&#x0003C;','&#60;','&#x02039;','&#8249;','&#x0227A;','&#8826;']
m = ['&#x0003E;','&#62;','&#x0203A;','&#8250;','&#x0227B;','&#8827;']
n = ['&#x0002F;','&#47;','&#x02044;','&#8260;']
o = ['&#x0005C;','&#92;','&#x02216;','&#8726;']
p = ['&#x00025;','&#37;']
q = ['&#x00040;','&#64;']
r = ['&#x000B2;','&#178;']
s = ['&#x000B3;','&#179;']
t = ['&#188;','&#x000BC;']
u = ['&#189;','&#x000BD;']
v = ['&#190;','&#x000BE;']
w = ['&#x0003A;','&#58;','&#x02236;','&#8758;']
     
html_entity = [a,b,c,d,e,f,g,h,j,k,l,m,n,o,p,q,r,s,t,u,v,w]

for i in range(0, len(list_replace)):
    if text.find(list_replace[i]) != -1:
        found.append(list_replace[i])
        text = text.replace(list_replace[i],random.choice(html_entity[i]))