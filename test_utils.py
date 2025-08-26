import unittest, math
import utils



class TestMeanCalculation(unittest.TestCase):
    
    
    def test_rounding1(self):
        prices = [237.33, 242.84, 248.13]
        expected_mean = sum(prices) / len(prices)
        expected = math.ceil(expected_mean * 100) / 100
        actualMean = utils.findMeanJustPrices(prices)
        self.assertEqual(actualMean, expected)
        print("Expected Mean: "+str(expected)+"\tActual Mean: "+str(actualMean))

    def test_rounding2(self):#change
        prices = [236, 227.63, 244.6]
        expected_mean = sum(prices) / len(prices)
        expected = math.ceil(expected_mean * 100) / 100
        actualMean = utils.findMeanJustPrices(prices)
        self.assertEqual(actualMean, expected)
        print("Expected Mean: "+str(expected)+"\tActual Mean: "+str(actualMean))

    def test_rounding3(self):#change
        prices = [245.55, 241.84, 217.9]
        expected_mean = sum(prices) / len(prices)
        expected = math.ceil(expected_mean * 100) / 100
        actualMean = utils.findMeanJustPrices(prices)
        self.assertEqual(actualMean, expected)
        print("Expected Mean: "+str(expected)+"\tActual Mean: "+str(actualMean))

if __name__ == '__main__':
    unittest.main()
