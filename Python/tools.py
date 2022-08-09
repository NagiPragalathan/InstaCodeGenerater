import random

#Global
vars : list = []

def CharToInt(String : str) -> list:
    Result : list = []
    for i in String:
        Result.append(ord(i))
        
    return Result
def IntToBite(String):
    Result : list = []
    out : list = []
    for i in String:
        Result.append(ord(i))
    for i in Result:
        out.append(i.to_bytes(10,"big"))
    return out
def IntToHex(String):
    Result : list = []
    out : list = []
    for i in String:
        Result.append(ord(i))
    for i in Result:
        out.append(hex(i))
    return out
def IntToOct(String):
    Result : list = []
    out : list = []
    for i in String:
        Result.append(ord(i))
    for i in Result:
        out.append(oct(i))
    return out
def IntToBin(String):
    Result : list = []
    out : list = []
    for i in String:
        Result.append(ord(i))
    for i in Result:
        out.append(bin(i))
    return out

def linked_lis(String : str,list : bool = False,shuffle : bool = True) -> list:
    linkList : list = [ [x,y] for y,x in enumerate(String)]
    if shuffle :
        random.shuffle(linkList)
        return linkList
    
def stringTochar(string : str) -> list:
    output:list = []
    for i in string:
        output.append(i)
    return output        


def varMaker(For : bool = False) -> str:
    length : list= [ i for i in range(4,7)]
    letters : list = [ chr(x) for x in range(65,91)]
    if For:
        return random.choice(letters)
    else:
        for y in range(97,123):
            letters.append(chr(y))
        len_ : int = random.choice(length)
        var : str = ""
        for i in range(len_):
            var : str = var + random.choice(letters)
        vars.append(var)
    return var
    
def strToVar(string : str,Var = True) -> list :
    lens : int = (int(len(string)/2)) if int(len(string)/2) > 0 else 6
    values : list = []
    start : int = 0
    out : list = []
    vars : list = []
    try:
        num : int = random.choice(range(3,lens))
        end : int = num 
        for i in range(len(string)):
            values.append(string[start:end])
            end : int = end + num
            start : int = start + num
        if(Var):
            for x,i in enumerate(values):
                if(i != ""):
                    a=varMaker()
                    out.append(f"""{a} = '{i}'""")
                    vars.append(a)
        else:
            for x,i in enumerate(values):
                if(i != ""):
                    a=varMaker()
                    out.append(a)
                    vars.append(a)
        return [out,vars]
    except:
        return [out,vars]
        
def twoDSplit(list_ : list,string: bool=True) -> str:
    str_ : str = ""
    listv : list = []
    if(string == True):
        for i in list_:
                str_ = str_ + i[0]
        return str_
    else: 
        for j in list_:
            listv.append(j[1])
        return listv
def vardic(NumOfVar:int):
    str_ : str = ""
    for i in range(NumOfVar+1):
        str_ = str_ + "var"+str(i+1)+" = varMaker()\n"
    return str_

#Alaining code.....
def HTML_Aliner(String : str) -> str:
    for i in range(len(String)):
        if( String[i] == "\n" ):
            String=String.replace(String[i],"</br>")
    for i in range(len(String)):
        if( String[i] == " " ):
            String=String.replace(String[i],"~&nbsp~")
    for i in range(len(String)):
        if( String[i] == "~" ):
            String=String.replace(String[i]," ")
    return String


def colors(String : str ) -> str:
    lis : list = ["Rhino", "artyclick", "DarkSkyblue","green", "symble", "Skyblue","yellow","pink"]
    KeyWords = {"Rhino" : ['False', 'None', 'True', 'assert', 'async', 'await', 'break', 'class', 'continue', 'elif', 'else', 'except', 
    'finally', 'for ', 'global', 'if ',"and ","or ","in ", 'lambda', 'nonlocal', 'not ', 'pass', 'raise', 'return ', 'try', 'while', 'with', 'yield'],
    "artyclick" : ["import ","from "]                          # #579d12
    ,"DarkSkyblue" : ["def"]  #9510b7                               ##0df109
    ,"green" : ["print"]                   # #3a7d1e
    ,"symble" : [ "]" , "[" ]
    ,"Skyblue" : vars,                                # #36a3f0
    "yellow" : ["str ","int ","list ","type "],
    "pink" : ["(",")"] }
    colors : str ={"Rhino":"#a586c0", "artyclick":"#579d12","DarkSkyblue":"#0df109", "green":"#b7881e", "symble":"#ebd114", "Skyblue":" #36a3f0","yellow":"#0df109","pink":"#eb14b3"}

    for i in lis:
        items : list = KeyWords.get(i)
        for j in items:
            String : str = f"""<span style="color: {colors.get(i)}">{ j }</span>""".join(String.split(j))
    return String


