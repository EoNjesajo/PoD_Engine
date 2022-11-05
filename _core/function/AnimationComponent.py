import os
import configparser
from ComponentBase import Component

class Animation_Component(Component):
    config = configparser.ConfigParser()
    config.read('config.ini')
    
    _path = ""
    _framesPerSecond = 60
    
    @staticmethod
    def set(**input):
        for key, value in input.items():
            exec(f"Animation_Component.{key} = value")

    @staticmethod    
    def load():
        pass
    
    @staticmethod
    def create():
        with open(os.path.join(Animation_Component._path, 'source', '4_animation.js'), 'w') as writer:
            for _, i in Animation_Component.config['ANIMATION'].items():
                exec('text =' + i)
                writer.write(locals()['text'])
        return os.path.join('source', '4_animation.js')
