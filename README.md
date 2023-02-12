# uniquefractions

This is code for:

* Creating a graph showing 'fraction uniqueness', or the proportion of fractions that are uniquely identifiable from a decimal/percentage as a function of the maximum possible denominator and the number of digits/degree of rounding.

showDenominatorRoundingGraph(max_denominator=1000, max_digits=7):
    """ this produces the graph showing the relationship between possible denominator size, number of digits in percentage, and proportion of uniques
    
    Args:
        max_denominator (optional - default is 1000): maximum possible denominator
        max_digits (optional - default is 7): maxium number of digits to include -- 
	more digits mean less rounding
    
    Returns:
        plt: pyplot of the relationship between possible denominator, number of digits, 
	and percent of uniquely identifiable fractions
          
    """

* Lets you input a numerator and denominator and tests to see how many possible other values there 
could be for various degrees of rounding, given a maximum possible denominator, returning the possible values:

testFractionValue(numerator, denominator, max_digits, max_denominator):
    """this lets you input a numerator and denominator and tests to see how many possible other values there
    could be for various degrees of rounding, using a max_denominator
    
    Args:
        numerator: numerator of fraction to test
        denominator: denominator of fraction to test
        max_digits: maxium number of digits to include -- more digits mean less rounding
        max_denominator: maximum possible denominator
        
    Returns:
        dfOutcomes: df showing the number and list of possible fraction analogues 
        at different numbers of digits/degrees of roundin
        
        returns "Your inputs will not work on this." if you inputs values that don't work
          
   """
*Lets you input a decimal value, number of digits/degree of rounding, and either max_denominator or true_denominator, and 
returns the count and list of possible fractions that it could be

testDecimalValue(decimal, digits, max_denominator=None, true_denominator=None):
    """this lets you input a decimal value under 1, the number of digits it's rounded to,
    and either a max_denominator or the true_denominator, and it returns a list of possible
    fraction values for it
    
    Args:
        decimal: value of decimal to test, like .5
        digits: number of digits that are included -- more digits mean less rounding
        max_denominator (optional): maximum possible denominator
        true_denominator (optionl): actual denominator
        
    Returns:
        possibleFractionValues: series with the count of possible fraction values for the decimal
        and the actual values

          
   """