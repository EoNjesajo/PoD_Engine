import os
import configparser
from ComponentBase import Component

class Scene_Component(Component):
    config = configparser.ConfigParser()
    config.read('config.ini')
    
    _path = ''
    _width= "window.innerWidth"
    _height = "window.innerHeight"

    @staticmethod
    def set(**input):
        for key, value in input.items():
            exec(f"Scene_Component.{key} = value")
        
    
    @staticmethod    
    def load():
        pass
    
    @staticmethod
    def create():
        with open(os.path.join(Scene_Component._path, 'source', '1_scene.js'), 'w') as writer:
            for _, i in Scene_Component.config['SCENE'].items():
                exec('text =' + i)
                writer.write(locals()['text'])
        return os.path.join('source', '1_scene.js')