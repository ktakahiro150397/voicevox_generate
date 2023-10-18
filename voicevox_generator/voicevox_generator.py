import logging
import pathlib
from voicevox_generator.voicevox_generated_data import voicevox_generated_data

class voicevox_generator():
    '''voicevoxの音声データを生成するクラス。'''

    def __init__(self) -> None:
        self.generate_directory:pathlib.Path = pathlib.Path("voicevox_generated")
        self.separators:list[str] = ["。","."]
        self.is_generate_byte_array:bool = False
        self.is_generate_file:bool = False
        self.generate_voice_list:list[voicevox_generated_data] = []

        self._logger = logging.getLogger(__name__)
        self._logger.addHandler(logging.NullHandler())
        self._logger.setLevel(logging.DEBUG)
        self._logger.propagate = True

    def generate_voice(self,generate_str:str) -> None:
        '''voicevoxの音声データを生成する。'''
        pass

    def delete_voice_all(self) -> None:
        '''生成した音声データを全て削除する。'''
        pass