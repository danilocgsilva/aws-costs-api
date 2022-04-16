import sys
sys.path.insert(1, "..")
from aws_costs_api.AWSCosts import AWSCosts
from tests.mocks.CostExplorerMock import CostExplorerMock
import unittest

class test_AWSCosts(unittest.TestCase):

    def test_fluent_interface_getCosts(self):
        awsCosts = AWSCosts()
        fakeProfile = 'mocked_profile'
        object_returned = awsCosts.setProfile(fakeProfile)
        self.assertTrue(
            isinstance(object_returned, AWSCosts)
        )

    def test_default_output_from_class(self):
        awsCosts = AWSCosts(CostExplorerMock())
        rawResults = awsCosts.getCosts()

        amount0 = rawResults["ResultsByTime"][0]["Total"]["BlendedCost"]["Amount"]
        amount1 = rawResults["ResultsByTime"][1]["Total"]["BlendedCost"]["Amount"]
        amount2 = rawResults["ResultsByTime"][2]["Total"]["BlendedCost"]["Amount"]
        self.assertEqual("0.821", amount0[:5])
        self.assertEqual("0.821", amount1[:5])
        self.assertEqual("0.820", amount2[:5])

