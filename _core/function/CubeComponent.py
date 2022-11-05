import os
import configparser
from ComponentBase import Component

class Cube_Component(Component):
    config = configparser.ConfigParser()
    config.read('config.ini')
    
    _path = ''
    _name = 'cube'
    _w = 1
    _d = 1
    _h = 1
    _color = 0x0087E6

    
    @staticmethod
    def set(**input):
        for key, value in input.items():
            exec(f"Cube_Component.{key} = value")

    @staticmethod    
    def load():
        pass
    
    @staticmethod
    def create():
        with open(os.path.join(Cube_Component._path, 'source', f'{Cube_Component._name}.js'), 'w') as writer:
            for _, i in Cube_Component.config['CUBE'].items():
                exec('text =' + i)
                writer.write(locals()['text'])
        return os.path.join('source', f'{Cube_Component._name}.js')