import os
import logging

from datetime import datetime

from config import ROOT_DIR


def make_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)


def create_logger():
    make_dir(ROOT_DIR + '/logs')

    # 로그 생성
    logger = logging.getLogger()

    # 로그의 출력 기준 설정
    logger.setLevel(logging.INFO)

    # log 출력 형식
    formatter = logging.Formatter('[%(asctime)s][%(levelname)s]::%(message)s')

    # log 출력
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    # log를 파일에 출력
    file_handler = logging.FileHandler(ROOT_DIR + f'/logs/{datetime.today().strftime("%Y%m%d")}_logs.log')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger


logger = create_logger()
