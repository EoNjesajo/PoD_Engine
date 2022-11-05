import sys
sys.path.append("_core/function")
from SystemEditor import System_Editor

if __name__ == '__main__':
    print("Welcome(write 'new' or 'load)'", end=' : ')
    control = input()
    if control == "new" : 
        print("Project name", end=' : ')
        _path = input()
        System_Editor.init_project(_path = _path)
    elif control == "load":
        raise NotImplemented
    
    while(True):
        print("Write Commend(write 'set' or 'run')'", end=' : ')
        control = input()
        if(control == 'set'):
            print("component name", end=' : ')
            component = input()
            print("setting", end=' : ')
            value = input()
            System_Editor.set_component(component = component, value = value)
            System_Editor.create_object(component)
        elif(control == 'run'):
            System_Editor.create_html()
        else :
            print("end")
            break