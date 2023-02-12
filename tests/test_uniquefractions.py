import uniquefractions
import unittest
 
class testgenDFOfNumeratorsAndDenominators(unittest.TestCase):
    def testLength(self):
        min_denominator=5
        max_denominator=50
        df=uniquefractions.genDFOfNumeratorsAndDenominators(max_denominator, min_denominator)
        self.assertEqual(len(df), 1311)
    def testAverageNumerator(self):
        min_denominator=5
        max_denominator=50
        df=uniquefractions.genDFOfNumeratorsAndDenominators(max_denominator, min_denominator)
        self.assertEqual(df['Numerator'].mean(), 16.842105263157894)
    def testAverageDenominator(self):
        min_denominator=5
        max_denominator=50
        df=uniquefractions.genDFOfNumeratorsAndDenominators(max_denominator, min_denominator)
        self.assertEqual(df['Denominator'].mean(), 33.68421052631579)
        
class testGenPercents(unittest.TestCase):
    def testRangeColumn(self):
        min_denominator=5
        max_denominator=50
        df=uniquefractions.genDFOfNumeratorsAndDenominators(max_denominator, min_denominator)
        max_digits=5
        dfPercent=uniquefractions.genPercents(df, max_digits)
        lastColumn=dfPercent.columns[-1]
        self.assertEqual(lastColumn, 'percent_rounded_5')
    def testValueColumns(self):
        min_denominator=5
        max_denominator=50
        df=uniquefractions.genDFOfNumeratorsAndDenominators(max_denominator, min_denominator)
        max_digits=5
        dfPercent=uniquefractions.genPercents(df, max_digits)
        sampleRowValue=dfPercent.iloc[80]['percent_rounded_5']
        self.assertEqual(sampleRowValue, 0.025640)
        
class testTestFractionValue(unittest.TestCase):
    def testDFLength(self):
        numerator=5
        denominator=11
        max_digits=5
        max_denominator=100
        fractionValues=uniquefractions.testFractionValue(numerator, denominator, max_digits, max_denominator)
        length=len(fractionValues)
        self.assertEqual(length, 5)
    def testlenDFValues(self):
        numerator=5
        denominator=11
        max_digits=5
        max_denominator=100
        fractionValues=uniquefractions.testFractionValue(numerator, denominator, max_digits, max_denominator)
        selectValues=fractionValues.iloc[-1].values[1]
        length=len(selectValues)
        self.assertEqual(length, 9)
    def testDFValues(self):
        numerator=5
        denominator=11
        max_digits=5
        max_denominator=100
        fractionValues=uniquefractions.testFractionValue(numerator, denominator, max_digits, max_denominator)
        selectValues=fractionValues.iloc[-1].values[1][-1]
        self.assertEqual(selectValues, '45/99')
            
class testTestDecimalValue(unittest.TestCase):
    def testLenValues(self):
        decimal=.4
        digits=3
        max_denominator=100
        decimalValues=uniquefractions.testDecimalValue(decimal, digits, max_denominator)
        length=len(decimalValues[1])
        self.assertEqual(length, 20)
    def testDFValues(self):
        decimal=.4
        digits=3
        max_denominator=100
        decimalValues=uniquefractions.testDecimalValue(decimal, digits, max_denominator)
        self.assertEqual(decimalValues[1][10], '22/55')
        
    
if __name__ == '__main__':
    unittest.main()