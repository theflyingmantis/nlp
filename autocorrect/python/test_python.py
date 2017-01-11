import collections
a = collections.defaultdict(lambda:0)
# a["hello"]=5
# print a["hello"]    #outputs 5
# print a["yo"] #outputs 0
# #the above will give error if we exclude lambda:0 term


from collections import defaultdict

# y = defaultdict(lambda: defaultdict(lambda: 0))
# print y["hello"]["world"]


trigram = collections.defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: 0)))
trigram ["A"]["S"]["d"] = 5
print trigram ["A"]["S"]["d"]