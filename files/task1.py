with open("dataset_24465_4.txt", "r") as r, open("output.txt", "w") as w:
    x = [f for f in r]
    x = x[::-1]
    for i in x:
        w.write(i)

""" with open('dataset_24465_4.txt') as inp, open('dataset_24465_4_write.txt', 'w') as out:
    [out.write('{}\n'.format(oln)) for oln in reversed([iln.rstrip() for iln in inp])]
    
    deleting every \n in every possible line with adding it again in every line to prevent missing it in new first 
    line """