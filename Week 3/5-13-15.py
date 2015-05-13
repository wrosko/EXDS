##x=3
##print x
##y=x
##print 'id of x', id(x)
##print 'id of y', id(y)
##print 'value of y is',y
##x=x+1
##print 'new x',x
##print 'new y', y
##
##a=[1,2]
##b=a
##print 'list a',a
##print 'list b',b
##print 'id of a and b',id(a), ',',id(b)
##
##a.append(3)
##print 'list a',a
##print 'list b',b
##print 'id of a and b',id(a), ',',id(b)
##
##s ='banana'
##t=s
##print 'string s is',s,'string t is',t
##print 'ids are s',id(s),'t',id(t)
##s=s+'s'
##print 'string s is',s,'string t is',t
##print 'ids are s',id(s),'t',id(t)
##s.replace('s','')
##print 'string s is',s,'string t is',t
##print 'ids are s',id(s),'t',id(t)



monthnumbers ={'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5}
print monthnumbers.keys()

keys=[]
values=[]
for month in monthnumbers:
    print month
    keys.append(month)
    values.append(monthnumbers[month])
    
print keys
print values


a =['Jan','Feb',3]
for i in a:
    print i

if 'Jan' in monthnumbers:
     monthnumbers['Jan']=monthnumbers['Jan']+1
     print 'value of jan increased by 1'
else:
    monthnumbers['Jan']=1
    print 'key created in dictionary'

print monthnumbers['Jan']
