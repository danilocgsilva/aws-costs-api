import sys
sys.path.insert(1, "..")
from aws_costs_api.AWSCosts import AWSCosts
import unittest

class test_AWSCosts(unittest.TestCase):

    def test_fluent_interface_getCosts(self):
        awsCosts = AWSCosts()
        fakeProfile = 'mocked_profile'
        object_returned = awsCosts.setProfile(fakeProfile)
        self.assertTrue(
            isinstance(object_returned, AWSCosts)
        )
