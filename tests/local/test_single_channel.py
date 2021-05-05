import unittest
from src.masonite.logging.channels import SingleChannel
import os
import pendulum

class TestSingleChannel(unittest.TestCase):

    def setUp(self):
        self.channel = SingleChannel()

    def test_channel_creates_file(self):
        self.channel.notice('This is a notice')
        self.fileExists('storage/logs/single.log')
    
    def fileExists(self, location):
        self.assertTrue(os.path.exists(location), "location '{}' does not exist".format(location))
        return self

    def test_exc_info(self):
        
        def raise_link(self):
            try:
                raise Exception('this is a first exception')
            except Exception as e:
                raise e

        def raise_link2(self):
            try:
                raise_link(self)
            except Exception as e:
                raise e

        try:
            raise_link2(self)
        except Exception as e:
            self.channel.error(e, exc_info=True)
            self.checkTraceInfo()
        
    def checkTraceInfo(self):
        fileContain = False
        with open("storage/logs/single.log", 'r') as read_obj:
            if "Traceback (most recent call last)" in read_obj:
                fileContain = True
        self.assertTrue(fileContain)
        