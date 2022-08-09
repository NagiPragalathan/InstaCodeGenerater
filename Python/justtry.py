from tools import CharToInt, linked_lis, varMaker, IntToHex, IntToBin, vardic, IntToBite, IntToOct, stringTochar, strToVar,twoDSplit

input_str = """🌟＿＿＿＿＿＿＿＿＿
    (ThinkingAboutYou..❤)
`  ￣￣🐬￣O ￣.￣￣￣
🐳    。    o         🐟  ＊   
╭━━━━━━╮┏╮╭┓
┃╰╯           ┃╰╮╭╯ 
┣━━╯        ╰━╯┃    
╰━━━━━━━━╯      
🌀🌀🌀🐠🐠🐠🌀🌀🐠🌀🌀a
💙🐙💙💙 💙💙💙💙""".split("\n")


#...................................................................................

variables = []
codes=[]
functions=[]
functioncall = []
imports = []
#...................................................................................



def Simple(string : str, type : int):
    if(type == 1):
        codes.append(f"""print("{string}")""")
        return f"""print("{string}")"""
    
    elif(type == 2):
        var1 = varMaker()
        fori = varMaker(For=True)
        
        code = f"""{var1} : list = []
for {fori} in "{string}" :
    {var1}.append({fori})

for i in {var1}:
    print( i, end = "" )
print()"""
        codes.append(f"""for {fori} in "{string}" :
    {var1}.append({fori})

for i in {var1} :
    print( i, end = "" )
print()""")
        variables.append(code.split("\n")[0])
        return code
    
    elif(type == 3):
        var1 = varMaker()
        code = f"""{var1} : list = [ x for x in "{string}" ]
for i in {var1} :
    print( i, end = "" )
print()"""
        codes.append(f"""for i in {var1}:
    print( i, end = "" )
print()""")
        variables.append(f"""{var1} : list = [ x for x in "{string}" ]""")

        return code
    
    elif(type == 4):
        var1 = varMaker()
        var2 = varMaker()
        
        code = f"""{var1} : list = [ chr(x) for x in {CharToInt(string)}]
{var2} : str = ""
for i in {var1}:
    {var2} : str = {var2} + i
print({var2})"""
        variables.append(f"""{var1} : list = [ chr(x) for x in {CharToInt(string)}]
{var2} : str = """"")
        codes.append(f"""for i in {var1}:
    {var2} : str = {var2} + i
print({var2})""")
        return code
    
    elif(type == 5):
        var1 = varMaker()
        code=f"""{var1}={string.split()}
for i in {var1} :
    print( i, end = " " )
print()"""          #..............................
        variables.append(code.split("\n")[0])
        codes.append(f"""for i in {var1} :
    print( i, end = " " )
print()""")
        
        return code
    
    elif(type == 6):
        var1 = varMaker()
        code = f"""{var1} : list = {list(string)}
for i in {var1} :
    print( i, end = "" )
print()"""
        variables.append(code.split("\n")[0])
        codes.append(f"""for i in {var1} :
    print( i, end = "" )
print()""")

        return code
    
    elif(type == 7):
        var1 = varMaker()
        code = f"""{var1} : list = {list(string[::-1])}
for i in {var1}[::-1] :
    print( i, end = "" )
print()"""
        variables.append(code.split("\n")[0])
        codes.append(f"""for i in {var1}[::-1] :
    print( i, end = "" )
print()""")
        return code
    
    elif(type == 8):
        var1 = varMaker()
        code=f"""{var1} : list = "{str(string[::-1])}"
print( {var1}[::-1] )"""
        variables.append(code.split("\n")[0])
        codes.append(f"""print( {var1}[::-1] )""")
        
        return code
    
    elif(type == 9):
        var1 = varMaker()
        fora = varMaker()
        code=f"""{var1} : list = lambda {fora} : {fora} + "{string[int(len(string)/2):][::-1]}"[::-1]
print( {var1}( "{string[:int(len(string)/2)]}" ) )"""
        variables.append(code.split("\n")[0])
        codes.append(f"""print( {var1}( "{string[:int(len(string)/2)]}" ) )""")
        

        return code
        
    elif(type==10):
        var1 = varMaker()
        code = f"""{var1} : list = {stringTochar(string)}
print( "".join( {var1} ) )"""
        variables.append(code.split("\n")[0])
        codes.append(f"""print( "".join( {var1} ) )""")
        
        
        return code
    elif(type==11):
        var1 = varMaker()
        strg = "{}"
        code = f"""{var1} : str = "{string[::-1]}"
print( "{strg}".format({var1}[::-1]) )"""
        variables.append(code.split("\n")[0])
        codes.append(f"""print( "{strg}".format({var1}[::-1]) )""")
        

        return code
    elif(type == 12):
        var1=varMaker()
        var2=varMaker()
        code = f"""{var1} : str = "{string}" + "..."
{var2} = {var1} * 4
print({var2}.split("...")[0])"""
        variables.append(f"""{var1} : str = {string}" + "..."
{var2} = {var1} * 4""")
        codes.append(f"""print({var2}.split("...")[0])""")
        

        return code
    elif(type == 13):
        val = strToVar(string)
        a="\n".join(val[0])
        str_ = ""
        for i in val[1]:
            str_ = str_ + i + "+"
        var1 = varMaker()
        code = f"""{a}\n{var1} : str = {str_[0:-1]} 
print({var1})"""
        variables.append(a)
        codes.append(f"""print({var1})""")
        
        return code
    elif(type == 14):
        val = strToVar(string,Var=False)[0]
        ll = linked_lis(val)
        lis = twoDSplit(ll,string=False)
        size = len(ll[0][0])
        st = twoDSplit(ll)
        var1=varMaker()
        var2=varMaker()
        code = f"""{var1}="{st}"
{var2} = {lis}
for i in range(len({var2})):
    for j in {var2}:
        if(i == j):
            print({var1}[j:j+{size}],end = "")
    """        
        variables.append(code.split("\n")[0:2])
        codes.append(f"""for i in range(len({var2})):
    for j in {var2}:
        if(i == j):
            print({var1}[j:j+{size}],end = "")""")
        

            
        return code
    
    elif(type == 15):
        var1=varMaker()
        var2=varMaker()
        value=IntToHex(string)
        code=f"""def {var2}({var1}) -> None :
    print("".join(chr(int(i,base=16)) for i in {var1}))
{var2}({value})"""
        codes.append(f"""def {var2}({var1}) -> None :
    print("".join(chr(int(i,base=16)) for i in {var1}))
{var2}({value})""")
        functioncall.append(f"""{var2}({value})""")

        return code
    
    elif(type == 16):
        var1=varMaker()
        var2=varMaker()
        var3=varMaker()
        
        code = f"""def {var2}({var3}):
        return {var2}
{var1}()"""
        codes.append(f"""def {var2}({var3}):
        return {var2}
{var1}()""")
        functioncall.append(f"""{var1}()""")

        return code
     
    
    
# print(Simple(input_str[4],2),variables,codes)
        
    
    
def hard(string : str,type : int):
    if(type == 1):
        var1 = varMaker()
        var2 = varMaker()
        forx = varMaker(For=True)
        fory = varMaker(For=True)
        fori = varMaker(For=True)
        
        
        code = f"""{var2} : str = ""
{var1} : list = {linked_lis(string)}
for {fori},{forx} in enumerate({var1}) :
    for j in range(len({var1})) :
        if({var1}[j][1] == {fori}) :
            {var2} : str = {var2} + {forx}[0]
print( {var2} )"""
        variables.append(f"""{var2} : str = ""
{var1} : list = {linked_lis(string)}""")
        codes.append(f"""for {fori},{forx} in enumerate({var1}) :
    for j in range(len({var1})) :
        if({var1}[j][1] == {fori}) :
            {var2} : str = {var2} + {forx}[0]
print( {var2} )""")
        return code
            
    elif(type == 2):
        var1 = varMaker()
        var2 = varMaker()
        forx = varMaker(For=True)
        fory = varMaker(For=True)
        fori = varMaker(For=True)
        
        code = f"""{var1} : str = ""
{var2} : list = {linked_lis(CharToInt(string))}
for {fori},{forx} in enumerate({var2}) :
    for {fory} in range( len({var2}) ) :
        if({var2}[{fory}][1] == {fori}) :
            {var1} : str = {var1} + chr( {forx}[0] )
print( {var1} )"""
        variables.append(f"""{var1} : str = ""
{var2} : list = {linked_lis(CharToInt(string))}""")
        codes.append(f"""for {fori},{forx} in enumerate({var2}) :
    for {fory} in range( len({var2}) ) :
        if({var2}[{fory}][1] == {fori}) :
            {var1} : str = {var1} + chr( {forx}[0] )
print( {var1} )""")
    
        return code

    if(type == 3):
        var1=varMaker()
        var2=varMaker()
        var3=varMaker()
        var4=varMaker()
        st="{}"
        code=f"""import random
def {var4}({var1},{var2}) -> None :
    if {var1} == 0 :
        print("{st}".format({var2}[::-1]))
    else:
        for i in {var2}[::-1] :
            print( i, end = "" )
        print()

{var3} : int =random.choice([0,1])
{var4}({var3},"{string[::-1]}")
"""
        imports.append(code[1])
        codes.append(f"""def {var4}({var1},{var2}) -> None :
    if {var1} == 0 :
        print("{st}".format({var2}[::-1]))
    else:
        for i in {var2}[::-1] :
            print( i, end = "" )
        print()
{var3} : int =random.choice([0,1])
{var4}({var3},"{string[::-1]}")
""")
        variables.append(f"""{var3}=random.choice([0,1])""")
        functioncall.append(f"""{var4}({var3},"{string[::-1]}")""")
        return code
   
   
    if(type == 4):
        val = strToVar(string)
        var1=varMaker()
        var2=varMaker()
        var3=varMaker(For=True)
        
        code=f"""def {var1}( **kid ) -> None :
        {var2} : list = {val[1]}
        print( "".join( [ kid[{var3}] for {var3} in {var2}] ) )

{var1}({",".join(val[0])})"""
        codes.append(f"""def {var1}( **kid ) -> None :
        {var2} : list = {val[1]}
        print( "".join( [ kid[{var3}] for {var3} in {var2}] ) )

{var1}({",".join(val[0])})""")
        functioncall.append(f"""{var1}({",".join(val[0])})""")
        return code
        
    if(type == 5):
        var1=varMaker()
        val = strToVar(string)
        var2=varMaker()
        a="\n"
        code = f"""{a.join(val[0])}
def {var1}({var2}) -> None :
    print( {var2} ,end = "" )
{a.join([var1+"("+i+")" for i in val[1]])}"""
        variables.append(a.join(val[0]))
        codes.append(f"""def {var1}({var2}) -> None :
    print( {var2} ,end = "" )
{a.join([var1+"("+i+")" for i in val[1]])}""")
        functioncall.append(f"""{a.join([var1+"("+i+")" for i in val[1]])}""")
        return code
     

# print(hard(input_str[-2],5),variables,codes,functioncall)
# hard(input_str[-2],5)

# E:\_Projects\ClassRoomTools\test\tools.py
    
# print(Simple(input_str[-2],7))

def ORD_Type(string : list,type : int):
    
    if( type == 1 ):
        var1=varMaker()
        var2=varMaker()
        fori=varMaker(For=True)
        code = f"""{var1} = { CharToInt(string) }
{var2} = ""
for {fori} in {var1}:
    {var2} = {var2} + chr({fori})
print({var2})"""
        variables.append(f"""{var1} = { CharToInt(string) }
{var2} = "" """)
        codes.append(f"""for {fori} in {var1}:
    {var2} = {var2} + chr({fori})
print({var2})""")
        return code
    
    elif( type == 2 ):
        var1=varMaker()
        var2=varMaker()
        fori=varMaker(For=True)
        code = f"""{var1} = { IntToOct(string) }
{var2} = ""
for {fori} in {var1}:
    {var2} = {var2} + chr(int({fori},8))
print({var2})"""
        variables.append(f"""{var1} = { IntToOct(string) }
{var2} = "" """)
        codes.append(f"""for {fori} in {var1}:
    {var2} = {var2} + chr(int({fori},8))
print({var2})""")
        return code
    elif( type == 3 ):
        var1=varMaker()
        var2=varMaker()
        fori=varMaker(For=True)
        code = f"""{var1} = { IntToHex(string) }
{var2} = ""
for {fori} in {var1}:
    {var2} = {var2} + chr(int({fori},16))
print({var2})"""
        variables.append(f"""{var1} = { IntToHex(string) }
{var2} = "" """)
        codes.append(f"""for {fori} in {var1}:
    {var2} = {var2} + chr(int({fori},16))
print({var2})""")
        return code
    
    elif( type == 4 ):
        var1=varMaker()
        var2=varMaker()
        fori=varMaker(For=True)
        code = f"""{var1} = { IntToBin(string) }
{var2} = ""
for {fori} in {var1}:
    {var2} = {var2} + chr(int({fori},2))
print({var2})"""
        variables.append(f"""{var1} = { IntToBin(string) }
{var2} = "" """)
        codes.append(f"""for {fori} in {var1}:
    {var2} = {var2} + chr(int({fori},2))
print({var2})""")
        return code
    elif( type == 5 ):
        var1=varMaker()
        var2=varMaker()
        fori=varMaker(For=True)
        code = f"""{var1} = { IntToBite(string) }
{var2} = ""
for {fori} in {var1}:
    {var2} = {var2} + chr(int.from_bytes({fori},"big"))
print({var2})"""
        variables.append(f"""{var1} = { IntToBite(string) }
{var2} = "" """)
        codes.append(f"""for {fori} in {var1}:
    {var2} = {var2} + chr(int.from_bytes({fori},"big"))
print({var2})""")
        return code
     

        
# print(ORD_Type(input_str[4],5))
    
def others(string:str,type:int):
    
    if(type == 1):
        var1 = varMaker()
        var2 = varMaker()
        value = [string[:int(len(string)/2)],string[int(len(string)/2):]]
        loop = f"print( next({var2}), end = '')\n"*len(value)+"print()"
        code = f"""{var1} = {value}
{var2} = iter({var1})
{loop}
        """
        variables.append(f"""{var1} = {value}
{var2} = iter({var1})""")
        codes.append(f"""{loop}""")
        return code
    elif(type == 2):
        var1=varMaker()
        var2=varMaker()
        var3=varMaker()
        var4=varMaker()
        value = CharToInt(string)
        code=f"""{var2} : str = open('{var1}.txt' , 'w')
{var2}.write(str({value}))
{var2}.close()
{var2} = open( '{var1}.txt', 'r' )
{var3} = {var2}.readline()
{var4}={var3}[1:-1].split(",")

for i in {var4} :
    print( chr( int( i ) ), end="" ) 
print()
"""

        codes.append(code)
        return code
    elif(type == 3):
        var1=varMaker()
        var2=varMaker()
        var3=varMaker()
        var4 = varMaker(For=True)
        val=IntToOct(string)
        code = f"""def {var2}({var3}) -> None:
  for {var4} in {var3} :
    print( chr (int( {var4}, base=8 ) ), end = "" )

{var1} = {val}

{var2}({var1})"""
        variables.append()
        codes.append(f"""def {var2}({var3}) -> None:
  for {var4} in {var3} :
    print( chr (int( {var4}, base=8 ) ), end = "" )

{var1} = {val}

{var2}({var1})
""")
        functioncall.append(f"""{var1} = {val}
{var2}({var1})""")
        return code
    
     
    
# others("hello",3)
    
def varcode():
    return [variables,codes]
    