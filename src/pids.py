import os
import sys
import subprocess
from services.processinfo import processInfo #pids.py depends of processinfo.py

'''
#==========================================================================================#
   This script was tested only on windows 

   v 1.0.0
#==========================================================================================#
'''

# ================================================== #
def getProcess(process):
    '''
        Get a particular process
        1) Get all process
        2) Find process
        3) Return all PID and USER process open.
    '''
    # Obtener las lineas de los procesos abiertos
    p = processInfo()

    # Procesamiento de las lineas
    # hago split por salto de linea y elimino encabezado y ultima linea
    lines = p.strip().split("\n")[3:-1]

    # Recorro lineas cortp por | y evaluo el proceso. Obtengo resultados si exiten
    for line in lines:
        cols = line.split("|")
        colProcess = cols[2].strip()

        if colProcess.lower() == process.lower():
            print(f"PID: {cols[1].strip()} USUARIOS: {cols[3].strip()}")

# ================================================== #

def killProcess(pid):
    '''
        kill process
        set PID to kill 
    '''
    subprocess.run(["taskkill", "/PID", pid, "/F"], shell=True)



# ================================================== #
def mainProcess():
    '''
    =================================================================================================================================================
        
        command basic: python pids.py <flag> <nameProcess or pid>

        flag => 
                --g : get process pids and usernames
                --k : kill process selected 
                --h : Help commmands
        
        nameProcess => process name => if os system is windows and if flat is diferent to --k set extension .exe if the nameProcess have not got it. 

        pid => Process id when you kill specific process

    ===================================================================================================================================================
    '''

    # Ingreso de argumentos
    try:
        args = sys.argv[1:]
    except IndexError:
        print("Debes ingresar el proceso a buscar")

    if len(args)==2:
        [flag, process]=args
    # Establecer el encoding dependiendo del os => subprocess => windows\linux
        encodig = ''
        if os.name == 'nt':
            encodig = "cp850"
        # Verificamos extension si estamos en windows setea .exe
            idx = process.find('.')
            if idx == -1 and flag != '--k':
                process = f"{process}.exe"
        elif os.name == 'psix':
            encodig = 'utf-8'   
        # select process
        if flag=='--g':
            getProcess(process)
        elif flag=='--k':
            killProcess(process)
        
    elif len(args)==1:
        [flag]=args

        if flag=='--h':
            help(mainProcess)
    
    print("==========================="+'\n'+"For help only set --h flag"+'\n'+"===========================")


# ================================================== #
mainProcess()
# ================================================== #
