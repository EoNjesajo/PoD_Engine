import os
import configparser
from ComponentBase import Component

class Camera_Component(Component):
    config = configparser.ConfigParser()
    config.read('config.ini')
    
    _path = ''
    _angle = 75
    _width= "window.innerWidth"
    _height = "window.innerHeight"
    _short = 0.1
    _long = 1000
    _x = 0
    _y = 0
    _z = 0
    
    @staticmethod
    def set(**input):
        for key, value in input.items():
            exec(f"Camera_Component.{key} = value")

    @staticmethod    
    def load():
        pass
    
    @staticmethod
    def create():
        with open(os.path.join(Camera_Component._path, 'source', '2_camera.js'), 'w') as writer:
            for _, i in Camera_Component.config['CAMERA'].items():
                exec('text =' + i)
                writer.write(locals()['text'])
        return os.path.join('source', '2_camera.js')
