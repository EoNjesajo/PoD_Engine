import sys
sys.path.append("_core/function")

import os
import configparser
import shutil

from AnimationComponent import Animation_Component 
from SceneComponent import Scene_Component 
from CameraComponent import Camera_Component 
from LightComponent import Light_Component 
from CubeComponent import Cube_Component


class System_Editor():
    config = configparser.ConfigParser()
    config.read('config.ini')

    _path = ''
    _lib = ["three.min.js"]
    _object = set()
    _source = []
    
    @staticmethod
    def init_project(_path = "Untitle"):
        System_Editor._path = _path
        os.makedirs(System_Editor._path, exist_ok=True)
        os.makedirs(os.path.join(System_Editor._path, 'build/lib'), exist_ok=True)
        os.makedirs(os.path.join(System_Editor._path, 'source'), exist_ok=True)
        init_component = ["Animation_Component","Scene_Component","Camera_Component", "Light_Component"]
        for i in init_component :
            System_Editor.set_component(component = i)
            System_Editor.create_object(component = i)
        System_Editor.create_html()
    
    def load_project(_path):
        pass

    @staticmethod
    def set_source():
        System_Editor._source.clear()
        for file in System_Editor._lib : 
            lib_name = os.path.join('build/lib', file)
            shutil.copyfile(os.path.join('_core/lib', file), os.path.join(System_Editor._path, lib_name))
            System_Editor._source.append(f'<script src="{lib_name}"></script>')

        for file in sorted(list(System_Editor._object)) : 
            System_Editor._source.append(f'<script src="{file}"></script>')

    @staticmethod
    def create_skeleton(frame, tab, writer):
        for key, value in frame.items():
            writer.write(tab + f'<{key}>' +'\n')
            if type(value) is dict:
                System_Editor.create_skeleton(value, tab + '\t', writer)
            else :
                for element in value:
                    writer.write(tab + '\t' + element +'\n')
            writer.write(tab + f'</{key}>' +'\n')
  

    @staticmethod
    def set_component(component, value=''):
        exec(f"{component}.set(_path = '{System_Editor._path}',{value})")

    @staticmethod
    def create_object(component):
        exec(f"System_Editor._object.add({component}.create())")

    
    @staticmethod
    def create_html():
        System_Editor.set_source()
        text = System_Editor.config['SKELETON']['DEFAULT']
        exec('frame = ' + text)
        writer = open(f'{System_Editor._path}/index.html', 'w')
        System_Editor.create_skeleton(locals()["frame"], '', writer)
        writer.close()  