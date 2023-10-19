import asyncio
from logging import NullHandler, getLogger
import pathlib
import re

from voicevox import AudioQuery, Client

from voicevox_generator.voicevox_generated_data import voicevox_generated_data

class voicevox_generator():
    '''voicevoxの音声データを生成するクラス。'''

    def __init__(self,*,logger = None) -> None:
        self.generate_directory:pathlib.Path = pathlib.Path("voicevox_generated")
        self.separators:list[str] = ["！","？","。","\."]
        self.is_generate_byte_array:bool = False
        self.is_generate_file:bool = False
        self.generate_voice_list:list[voicevox_generated_data] = []

        self.voicevox_client:Client = Client()

        self._logger = logger or getLogger(__name__)
        self._logger.addHandler(NullHandler())
        self._logger.propagate = True

    async def generate_voice_multi(self,generate_str:str) -> None:
        # 文章をセパレータで区切る
        generate_str_list = self.__get_generate_str(generate_str)

        # 区切った文章ごとに音声クエリを取得
        # タスクリストを作成
        audio_query_task_list = []
        for generate_str_elem in generate_str_list:
            audio_query_task_list.append(self.voicevox_client.create_audio_query(generate_str_elem,speaker=1))
            self._logger.info(f"audio_queryを作成:{generate_str_elem}")

        # タスクを実行・結果を取得
        audio_query_list = await asyncio.gather(*audio_query_task_list)
        self._logger.info("audio_queryを取得")

        audio_data_zip = await self.voicevox_client.multi_synthesis(audio_query_list,speaker=1)
        self._logger.info("audio_dataを取得")

        with open("generate_voice_multi.zip","wb") as f:
            f.write(audio_data_zip)

        self._logger.info("音声データの取得に成功しました。")
        
    async def generate_voice(self,generate_str:str) -> None:
        '''voicevoxの音声データを生成する。'''
        async with Client() as client:
            self._logger.info("voicevoxに接続しました。")

            audio_query = await self.voicevox_client.create_audio_query(generate_str,speaker=1)
            self._logger.info("audio_queryを取得")

            audio_data = await audio_query.synthesis(speaker=1)
            self._logger.info("audio_dataを取得")

            self._logger.info("音声データの取得に成功しました。")

            with open("test.wav","wb") as f:
                f.write(audio_data)

    async def generate_voice_pararell(self,generate_str:str) -> None:
        # 文章をセパレータで区切る
        generate_str_list = self.__get_generate_str(generate_str)

        # 区切った文章ごとに音声クエリを取得
        # タスクリストを作成
        audio_query_task_list = []
        for generate_str_elem in generate_str_list:
            audio_query_task_list.append(self.__create_audio_query_and_audio_data(generate_str_elem))

        # タスクを実行
        await asyncio.gather(*audio_query_task_list)

    async def __create_audio_query_and_audio_data(self,generate_str:str) -> None:
        '''音声クエリと音声データを生成する。'''
        audio_query = await self.voicevox_client.create_audio_query(generate_str,speaker=1)
        self._logger.info("audio_queryを取得")

        audio_data = await audio_query.synthesis(speaker=1)
        self._logger.info("audio_dataを取得")

        with open(f"pararell/generate_voice_{generate_str}.wav","wb") as f:
            f.write(audio_data)

        self._logger.info(f"音声データの取得に成功しました。: {generate_str}")

    def __get_generate_str(self,generate_str:str) -> list[str]:
        # 区切り文字で文章を区切る
        pattern = "|".join(self.separators)
        generate_str_list = re.split(pattern,generate_str)

        return generate_str_list

    def delete_voice_all(self) -> None:
        '''生成した音声データを全て削除する。'''
        pass