# -*- coding: utf-8 -*-
"""

"""
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

def genDFOfNumeratorsAndDenominators(max_denominator):
    # we exclude 0s from the denominator; we add 1 to be inclusive of the max_denominator value
   df = pd.DataFrame([[x, y] for x in range(max_denominator + 1)
                      for y in range(1, max_denominator + 1) if y >= x])
   df.columns=["Numerator", "Denominator"]
   return(df)
   
def genPercents(df, max_digits):
    # this generates rounded percentages varying by degree of rounding
    df['Percent']=df['Numerator']/df['Denominator']
    for digits in range(1, max_digits+1):
        var_name=f"percent_rounded_{digits}"
        df[var_name]=df['Percent'].round(digits)
    return(df)

def testValue(df, numerator, denominator):
   # this lets you input a numerator and denominator and tests to see how many possible other values there
   # could be for various degrees of rounding, using the max_denominator in the df
   max_digits=deriveMaxDigits(df)
   if numerator>denominator or denominator==0 or denominator>df['Denominator'].max():
      print("Your inputs will not work on this.")
   else:
      max_denominator=df['Denominator'].max()
      rowsForAppend=[]
      row=df.loc[(df['Numerator']==numerator) & (df['Denominator']==denominator)]
      for digits in range(1, max_digits+1):
         var_name=f"percent_rounded_{digits}"
         percent_by_rounding=row[var_name].iloc[0]
         all_options=df.loc[df[var_name]==percent_by_rounding]
         all_options_values = [
             f"{str(i[0])}/{str(i[1])}"
             for i in all_options[['Numerator', 'Denominator']].values
         ]
         print(f"There are {len(all_options)} possible numerator/denominator combinations for that value at {digits} digits of rounding for a maximum possible denominator of {max_denominator}.")
         rowsForAppend.append([digits, len(all_options), all_options_values])
      dfOutcomes=pd.DataFrame(rowsForAppend)
      dfOutcomes.columns=["Digits", "Number of Possibilities", "List of Possibilities"]
      dfOutcomes.name = f'Percent analogues of {str(numerator)}/{str(denominator)}'
      dfOutcomes=dfOutcomes.set_index("Digits")
      return(dfOutcomes)
            
def deriveMaxDigits(df):
   return max(int(i[-1]) for i in df.columns if i[-1].isdigit())     

def generateGraphofUniqueIdentifiers(df):
   # this generates a table showing the proportion of unique values by possible numerator/denominator pairs, given level of rounding and the size of the possible denominator
   listofAnswers=[]
   max_digits=deriveMaxDigits(df)
   max_denominator=df['Denominator'].max()
   denominator_limits=[i for i in [100, 200, 500, 1000, 2000, 5000, 10000] if i<=max_denominator]
   for digits in range(1, max_digits):
       var_name=f"percent_rounded_{digits}"
       for denominator_limit in denominator_limits:
           subset=df.loc[df['Denominator']<=denominator_limit]
           values=subset[var_name].value_counts().value_counts()
           try:
               identified_perfect=values.loc[1]/len(subset)
           except:
               identified_perfect=0
           listofAnswers.append([digits, denominator_limit, identified_perfect])
   answers=pd.DataFrame(listofAnswers)
   answers.columns=['Rounding Digits', 'Denominator Maximum', 'Percentage Identified Perfectly']
   return pd.pivot(
       answers,
       index='Rounding Digits',
       columns='Denominator Maximum',
       values='Percentage Identified Perfectly',
   )

def showGraph():
    # this produces the graph showing the relationship between possible denominator size, number of digits in percentage, and proportion of uniques
    dataForGraph=generateGraphofUniqueIdentifiers(df)
    x=dataForGraph.index
    for col in dataForGraph.columns:
        plt.step(x, y=dataForGraph[col], label =col, alpha=.8)
    plt.legend(title="Max Denominator")
    plt.title("Percent of Unique Fractions by Total Possible Denominator, Number of Digits in Percent")
    plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter(xmax=1.0))
    plt.xlabel("Number of digits given in percentage")
    plt.ylabel("Perecent of Unique Fractions")
    plt.show()
    
df=genDFOfNumeratorsAndDenominators(1000)
df=genPercents(df,7)
testValues=testValue(df, 3, 7)
showGraph()
