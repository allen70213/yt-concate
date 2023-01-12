import os

import yt_dlp
import webvtt

from yt_concate.pipeline.steps.step import Step
from yt_concate.pipeline.steps.step import StepException
from yt_concate.utils import Utils


class DownloadCaptions(Step):
    def process(self, data, inputs, utils):

        for url in data:
            if utils.caption_file_exists(url):
                print('found existing caption file')
                continue

            SAVE_PATH = '/'.join(os.getcwd().split('/')[:3]) + '\downloads\captions'
            ydl_opts = {
                'writesubtitles': True,
                'writeautomaticsub': True,
                'skip_download': True,
                'subtitleslangs': ['en'],
                'outtmpl': SAVE_PATH
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
