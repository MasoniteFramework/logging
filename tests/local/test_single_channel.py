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