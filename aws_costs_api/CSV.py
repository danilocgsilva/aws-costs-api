from aws_costs_api.AWSCosts import AWSCosts


class CSV:

    def setAWSCostsClass(self, awsCostsClass: AWSCosts):
        self.awsCosts = awsCostsClass
        return self

    def getCsv(self):
        rawData = self.awsCosts.getCosts()

        stringData = ""

        for cellData in rawData["ResultsByTime"]:
            stringData += cellData["TimePeriod"]["Start"] + " - " + cellData["TimePeriod"]["Start"] + ", "
            stringData += cellData["Total"]["BlendedCost"]["Amount"] + "/n"

        return stringData
