import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

def genDFOfNumeratorsAndDenominators(max_denominator, min_denominator=0):
    """this generates all of the possible numberator/denominator fractions that are between 
    zero and one, given the min and max denominators
    
    Args:
        max_denominator: maximum possible denominator
        min_denominator (optional - defaul is 0): minimum possible denominator
        
    Returns:
        df: pandas df with all combinations of numerators and denominators
          
   """
    df = pd.DataFrame([[x, y] for x in range(min_denominator, max_denominator + 1)
                      for y in range(1, max_denominator + 1) if y >= x])
    df.columns=["Numerator", "Denominator"]
    return(df)

def genPercents(df, max_digits):
    """this generates all of the possible numberator/denominator fractions that are between 
    zero and one, given the min and max denominators
    
    Args:
        df: pandas df with all combinations of numerators and denominators
        max_digits: maxium number of digits to include -- more digits mean less rounding
        
    Returns:
        df_with_rounded_digits: df with additional variables showing percent for varying degree of roundedness
          
   """
    df['Percent']=df['Numerator']/df['Denominator']
    for digits in range(1, max_digits+1):
        var_name=f"percent_rounded_{digits}"
        df[var_name]=df['Percent'].round(digits)
    df_with_rounded_digits=df
    return(df_with_rounded_digits)

def testValue(df, numerator, denominator):
    """this lets you input a numerator and denominator and tests to see how many possible other values there
    could be for various degrees of rounding, using the max_denominator in the df
    
    Args:
        df: pandas df with all combinations of numerators and denominators
        numerator: numerator of fraction to test
        denominator: denominator of fraction to test
        
    Returns:
        dfOutcomes: df showing the number and list of possible fraction analogues 
        at different numbers of digits/degrees of roundin
        
        returns "Your inputs will not work on this." if you inputs values that don't work
          
   """
    max_digits=deriveMaxDigits(df)
    if numerator>denominator or denominator==0 or denominator>df['Denominator'].max():
        return("Your inputs will not work on this.")
    else:
      max_denominator=df['Denominator'].max()
      row=df.loc[(df['Numerator']==numerator) & (df['Denominator']==denominator)]
      rowsForAppend = [
          returnRowForPossibleOptions(df, row, digits, max_denominator)
          for digits in range(1, max_digits + 1)
      ]
      dfOutcomes=pd.DataFrame(rowsForAppend)
      dfOutcomes.columns=["Digits", "Number of Possibilities", "List of Possibilities"]
      dfOutcomes.name = f'Percent analogues of {str(numerator)}/{str(denominator)}'
      dfOutcomes=dfOutcomes.set_index("Digits")
      return(dfOutcomes)

def returnRowForPossibleOptions(df, row, digits, max_denominator):
    """this takes a row of a pandas df and returns all possible fractions associated with that row
    
    Args:
        df: pandas df with all combinations of numerators and denominators
        digits: the number of digits/degree of rounding for the calculation
        max_denominator: maximum possible denominator
        
    Returns:
        digits: the number of digits/degree of rounding for the calculation
        len(all_options): count of all possible fraction analogues
        all_options_values: list of all possile fraction analogues
        

   """
    var_name=f"percent_rounded_{digits}"
    percent_by_rounding=row[var_name].iloc[0]
    all_options=df.loc[df[var_name]==percent_by_rounding]
    all_options_values =  [f"{str(i[0])}/{str(i[1])}" for i in all_options[['Numerator', 'Denominator']].values]
    return([digits, len(all_options), all_options_values])

def deriveMaxDigits(df):
    """this takes a df and returns the maximum number of digits 
    that are included in it for the percentage calculations
    
    Args:
        df: pandas df with all combinations of numerators and denominators

    Returns:
        max_digits: maxium number of digits of rounding that are included in the df
          
   """
    max_digits=max(int(i[-1]) for i in df.columns if i[-1].isdigit())
    return(max_digits)

def generatePercentIdentifiedPercent(df, digits, max_denominator, var_name):
    """this shows what percentage of fractions can be uniquely identified
    
    Args:
        df: pandas df with all combinations of numerators and denominators
        digits: the number of digits/degree of rounding for the calculation
        max_denominator: maximum possible denominator
        var_name: string for naming the returned column

    Returns:
        digits: the number of digits/degree of rounding for the calculation
        max_denominator: maximum possible denominator
        identified_perfect: percent of fractions that can be uniquely identified, given 
        the max denominator and level of rounding
          
    """
    subset=df.loc[df['Denominator']<=max_denominator]
    values=subset[var_name].value_counts().value_counts()
    try:
        identified_perfect=values.loc[1]/len(subset)
    except:
        identified_perfect=0
    return([digits, max_denominator, identified_perfect])

def generateGraphofUniqueIdentifiers(df):
    """ this generates a table showing the proportion of unique values by possible numerator/denominator pairs, 
    given level of rounding and the size of the possible denominator
    
    Args:
        df: pandas df with all combinations of numerators and denominators


    Returns:
        pivoted: df showing the percent of perfectly-identified fractions for different values
        of max denominator and digits (degree of rounding)
          
    """
    listofAnswers=[]
    max_digits=deriveMaxDigits(df)
    max_denominator=df['Denominator'].max()
    denominator_limits=[i for i in [100, 200, 500, 1000, 2000, 5000, 10000] if i<=max_denominator]
    for digits in range(1, max_digits+1):
        var_name=f"percent_rounded_{digits}"
        listofAnswers.extend(
            generatePercentIdentifiedPercent(df, digits, denominator_limit,
                                           var_name)
            for denominator_limit in denominator_limits)
    answers=pd.DataFrame(listofAnswers)
    answers.columns=['Rounding Digits', 'Denominator Maximum', 'Percentage Identified Perfectly']
    pivoted=pd.pivot(
        answers, index='Rounding Digits', columns='Denominator Maximum', values='Percentage Identified Perfectly')
    return(pivoted)

def showGraph(max_denominator=1000, max_digits=7):
    """ this produces the graph showing the relationship between possible denominator size, number of digits in percentage, and proportion of uniques
    
    Args:
        max_denominator (optional - default is 1000): maximum possible denominator
        max_digits (optional - default is 7): maxium number of digits to include -- more digits mean less rounding
    
    Returns:
        plt: pyplot of the relationship between possible denominator, number of digits, and percent of uniquely identifiable fractions
          
    """
    df=genDFOfNumeratorsAndDenominators(max_denominator)
    df=genPercents(df,max_digits)
    dataForGraph=generateGraphofUniqueIdentifiers(df)
    x=dataForGraph.index
    for col in dataForGraph.columns:
        plt.step(x, y=dataForGraph[col], label =col, alpha=.8)
    plt.legend(title="Max Denominator")
    plt.title("Percent of Unique Fractions by Total Possible Denominator, Number of Digits in Percent")
    plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter(xmax=1.0))
    plt.xlabel("Number of digits given in percentage")
    plt.ylabel("Perecent of Unique Fractions")
    return(plt)

