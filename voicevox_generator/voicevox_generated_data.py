import logging
import pathlib

class voicevox_generated_data():
    '''voicevoxの生成データを格納するクラス'''

    def __init__(self) -> None:
        self.generate_str:str = ""
        self.generate_voice_byte_array:bytes = None
        self.generate_voice_file:pathlib.Path = None
        self.is_generate_byte_array:bool = False
        self.is_generate_file:bool = False

        self._logger = logging.getLogger(__name__)
        self._logger.addHandler(logging.NullHandler())
        self._logger.setLevel(logging.DEBUG)
        self._logger.propagate = True

    def delete(self) -> None:
        '''生成データを削除する'''

        # バイト配列が存在する場合は削除する
        if self.generate_voice_byte_array is not None:
            self.generate_voice_byte_array = None
        
        # ファイルが存在する場合は削除する
        if self.generate_voice_file is not None:
            if self.generate_voice_file.exists():
                self.generate_voice_file.unlink()
                self._logger.debug(f"delete file:{self.generate_voice_file}")
                self.generate_voice_file = None