from icrawler.builtin import BingImageCrawler
import sys
import os

crawler=BingImageCrawler(storage={"root_dir":"c:\\python_work\\idle\\download"})

crawler.crawl(keyword="世界遺産",max_num=10)