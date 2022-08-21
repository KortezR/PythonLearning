import re

line1 = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""
matches1 = re.findall("dutch", line1, re.IGNORECASE)
print(matches1)
line2 = "Москва: 777, 999, 797. Тула: 071, 950, 112."
matches2 = re.findall("\d", line2)
print(matches2)
line3 = "Привидение прошуршало и и исчезло в углу."
matches3 = re.findall(".ло", line3)
print(matches3)