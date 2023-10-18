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
    await generator.generate_voice("こんにちは")

if __name__ == "__main__":
    asyncio.run(main())