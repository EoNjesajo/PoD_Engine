import os
import configparser
from ComponentBase import Component

class Light_Component(Component):
    config = configparser.ConfigParser()
    config.read('config.ini')
    
    _path = ""
    _color = 0x808080
    
    @staticmethod
    def set(**input):
        for key, value in input.items():
            exec(f"Light_Component.{key} = value")
   
    @staticmethod    
    def load():
        pass
    
    @staticmethod
    def create():
        with open(os.path.join(Light_Component._path, 'source', '3_light.js'), 'w') as writer:
            for _, i in Light_Component.config['LIGHT'].items():
                exec('text =' + i)
                writer.write(locals()['text'])
        return os.path.join('source', '3_light.js')
