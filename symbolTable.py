
# coding: utf-8

# In[1]:


#Sybol_Table


# In[8]:


input_file = """
int a , b , c ;
float d , e ;
a = b = t 5 ;
c = 6 ;
if ( a > b )
{
    c = a - b ;
    e = d - 2.0 ;
}
else
{
    d = e + 6.0 ;
    b = a + c ;
}
"""


# In[4]:


mathoperator = [ '+','-','*','/','=','+=','-=','*=','/=','%=']
keyword = ['False','class','finally','is','return','None','continue','for','lambda','try','True',
           'def','from','nonlocal','while','and','del','global','not','with','as','elif','if','or',
           'yield','assert','else','import','pass','break','except','in','raise','char','break',
           'continue','goto','if','else','double','float','long','int','register','return','void',
           'static','volatile','case','const','default','do','enum','extern','for','sizeof','sign',
           'struct','switch','unsighed']
logical  = ['==','&&','||','!=','!','<','>','<=','>=']
bitwise = ['&','|','>','<','^','~','<<','>>']
other = [',','(',')','{','}',';','[',']']


          


# In[16]:


def lexical_analyzer (input_file):
    return input_file.split()


# In[13]:


def symbol_table (inputs):
    m = []
    k = []
    l = []
    b = []
    o = []
    n = []
    i = []
    f = []

    for data in inputs:
        if data in keyword:
            if data not in k:
                k.append(data)
        elif data in mathoperator:
            if data not in m:
                m.append(data)
        elif data in logical:
            if data not in l:
                l.append(data)
        elif data in bitwise:
            if data not in b:
                b.append(data)
        elif data in other:
            if data not in o:
                o.append(data)
        else:
            try:
                num = float(data)
                if num not in f:
                    f.append(data)
            except:
                if data not in i:
                    i.append(data)
                    
    outputs= {
        'keywords are' : k,
        'identifiers are' : i,
        'math operators are' : m,
        'logical operators are'  : l+b,
        'numerical values are' : n+f,
        'others are' : o
        
        
    }
    return outputs
    


# In[17]:


L = lexical_analyzer(input_file)
s_table = symbol_table(inputs=L)
for x in s_table:
    print (x,':',s_table[x])
    

