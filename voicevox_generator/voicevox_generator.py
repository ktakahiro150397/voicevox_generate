from logging import NullHandler, getLogger
import pathlib
from voicevox_generator.voicevox_generated_data import voicevox_generated_data
from voicevox import Client

class voicevox_generator():
    '''voicevoxの音声データを生成するクラス。'''

    def __init__(self,*,logger = None) -> None:
        self.generate_directory:pathlib.Path = pathlib.Path("voicevox_generated")
        self.separators:list[str] = ["。","."]
        self.is_generate_byte_array:bool = False
        self.is_generate_file:bool = False
        self.generate_voice_list:list[voicevox_generated_data] = []

        self._logger = logger or getLogger(__name__)
        self._logger.addHandler(NullHandler())
        self._logger.propagate = True

    async def generate_voice(self,generate_str:str) -> None:
        '''voicevoxの音声データを生成する。'''
        async with Client() as client:
            self._logger.debug("voicevoxに接続しました。")

            audio_query = await client.create_audio_query(generate_str,speaker=1)
            self._logger.info("audio_queryを取得")

            audio_data = await audio_query.synthesis(speaker=1)
            self._logger.info("audio_dataを取得")

            self._logger.debug("音声データの取得に成功しました。")

            with open("test.wav","wb") as f:
                f.write(audio_data)

    def delete_voice_all(self) -> None:
        '''生成した音声データを全て削除する。'''
        pass