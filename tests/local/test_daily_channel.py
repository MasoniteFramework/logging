import unittest
from src.masonite.logging.channels import DailyChannel
import os
import pendulum

class TestDailyChannel(unittest.TestCase):

    def setUp(self):
        self.channel = DailyChannel()
        self.today = pendulum.now().in_tz('UTC').to_date_string()

    def test_channel_creates_file(self):
        self.channel.notice('This is a notice')
        self.fileExists('storage/logs/{}.log'.format(self.today))
    
    def fileExists(self, location):
        self.assertTrue(os.path.exists(location), "location '{}' does not exist".format(location))
        return self