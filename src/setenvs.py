import os
import sys



def setEnvs(env, n):
    if(n!='n'):
        [name, path]=env
        os.environ[name]=path
    else:
        for e in env:
            [name, path]=e
            os.environ[name]=path


def getEnvs(name):
    res=os.environ.get(name)
    return res


def seletTypeFunction(setting, envs):
    res=[]
    if setting.lower()=='--n':
        fenvs=envs.split(',')
        for f in fenvs:
            f=f.split('=')
            res.append(f)
    elif setting.lower()=='--file':
        try:
            with open(envs) as outline:
                for l in outline:
                    res.append(l.strip().split('='))
        except Exception:
            print("Path could no be found")
    elif setting.lower()=='--s':
        res=envs.split('=')
    elif setting.lower()=='--g':
        res=envs

    return res


            
def mainEnv():
    '''
    flag=> --get \\ --set
        if get or set => 
            if --n you can pas nameEnvs with "," if set=> nameenv1=env1,nameenv2=env2...
            else if not --n=> only one nameEnv

            if --file =>
                you do not pass --n this set in default mode
            elif --n =>
                you do not pass --file and you neet pass nameEnvs with ",".

            if no --n and --file
                you can only pass ona nameEnv
    .s=> single set settig --s 
    .g=> single get settihng

    .n=> --n => if --n=> more that one enviroments else if not --n => only one env. => only for set.
    .file=> if --file => yo neet to pass the path to file location => file location need have NAME=ENV structure strings. 
    envs=> if --n => pass => nameenv1=env1,nameenv2=env2... else nameenv=env
    '''
    [flag, setting, envs]=sys.argv[1:]
    # Arguments number control
    res=seletTypeFunction(setting, envs)

    if flag.lower()=='--get':
       getEnvs(res)

    elif flag.lower()=='--set':
       setEnvs(res,"s")

mainEnv()
