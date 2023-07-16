class ClientParametersMock:

    def getClientParameterValues(self):
        return {
            "TimePeriod": {
                "Start": "2023-05-22",
                "End": "2023-06-22"
            },
            "Granularity": "DAILY",
            "Metrics": [
                "BlendedCost"
            ]
        }