from django.db import models
from django.db.models import Q
import random, html
import re, pandas as pd
import pandasql as ps


class Words(models.Model):

    words = models.TextField()

    def __str__(self):
        return self.words

    def spinWord(self, artikel):
        text = str(artikel)

        list_txt = [x.replace('\n', '').replace('.', '').replace(',', '') for x in text.split(" ")]
        stopwords = list(StopWords.objects.all().values('stop_words'))
        list_stopwords = []
        for w in stopwords:
            list_stopwords.append(w["stop_words"])
        
        list_txt = [x for x in list_txt if x not in list_stopwords]
        
        random_list_txt = random.sample(list_txt, round(len(list_txt)/2))

        for w in random_list_txt:
            try:
                filter = Q(words__istartswith=w+',') | Q(words__iendswith=','+w) | Q(words__iendswith=', '+w) | Q(words__icontains=','+w+',') | Q(words__icontains=', '+w+',') 
                syn = list(Words.objects.filter(filter))
                if syn:
                    df_sin = pd.DataFrame(syn)
                    df_sin = df_sin.rename(columns={0:'word'})[['word']]
                    sample = df_sin.sample(1)['word']
                    selected = random.choice(str(sample[sample.index[0]]).split(", "))
                    text = text.replace(w, selected)
            except Exception as e:
                print(str(e))

        return text

    def spinNegative(self, artikel):
        text = str(artikel)

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

        for i in range(0, len(negative)):
            if text.find(negative[i]) != -1:
                found.append(negative[i])
                text = text.replace(negative[i],replace_with[i])

        for i in range(0, len(list_replace)):
            if text.find(list_replace[i]) != -1:
                found.append(list_replace[i])
                text = text.replace(list_replace[i],random.choice(html_entity[i]))
                text = html.unescape(text)
        return text

class StopWords(models.Model):

    stop_words = models.CharField(max_length=50)

    def __str__(self):
        return self.stop_words