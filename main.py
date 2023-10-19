import json

from logging import config, getLogger
import os
import asyncio

from voicevox_generator.voicevox_generator import voicevox_generator

# 現在のスクリプトファイルの絶対パスを取得する
script_dir = os.path.dirname(os.path.abspath(__file__))

# 設定ファイルのパスを作成する
settings_file_path = os.path.join(script_dir, "logsettings.json")

# ログ設定読込
with open(settings_file_path) as f:
    config.dictConfig(json.load(f))

logger = getLogger(__name__)

async def main():
    logger.debug('debug')
    logger.info('info')
    logger.warning('warning')
    logger.error('error')
    logger.critical('critical')


    generator = voicevox_generator()

    test_str = "こんにちは。これは複数文章テスト用の文字列です。" \
    "multiとそうではないバージョンで、文字列生成に差が発生するのかどうか？" \
    "それとも以外と差がないのか？" \
    "テストしてみます。" \
    "以下は適当な文章です。" \
    "もうちょっとひねった文章を作成したいです。" \
    "私は猫です。" \
    "私は犬です。" \
    "私は鳥です。" \
    "私は魚です。" \
    "私は人間です。" \
    "私はロボットです。" \
    "私は宇宙人です。"

    logger.info('generate_voice 開始')
    await generator.generate_voice(test_str)
    logger.info('generate_voice 完了')

    logger.info('generate_voice_multi 開始')
    await generator.generate_voice_multi(test_str)
    logger.info('generate_voice_multi 完了')

    logger.info('generate_voice_pararell 開始')
    await generator.generate_voice_pararell(test_str)
    logger.info('generate_voice_pararell 完了')

if __name__ == "__main__":
    asyncio.run(main())