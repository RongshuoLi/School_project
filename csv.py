
fileobj = open("covid_data.csv","r") # r,w or a are the options
delfirst = fileobj.readline()
datalist = fileobj.readlines()
fileobj.close()

conflist = []
for country in datalist:
    templist = country.split(",")
    pname = templist[2]
    cname = templist[3]
    lat = templist[5]
    lon = templist[6]
    conf = int(templist[7])
    #print(pname + cname + lat + lon + conf)
    conflist.append({"pname":pname,"cname":cname,"lat":lat,"lon":lon,"conf":conf})

#print(conflist)
conflist.sort(key=lambda s: s['conf'], reverse=True)
fileout = open("covid_data.js","w")
fileout.write("data = " + str(conflist))
fileout.close()
