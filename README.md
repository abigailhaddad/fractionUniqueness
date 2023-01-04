# fractionUniqueness

This is code for:

* Taking a numerator/denominator pair and determining, given a maximum possible denominator, how many other fractions will have the same percentage value, given various possible values of rounding. 
For instance, if you input 3 and 7 (for 3/7), with a maximim denominator of 1,000, a 4-digit rounding gives you a value of 0.4286. If we have a possible denominator of up to 1,000, there are 142 other values with that same percentage.
If you input a 19 and 289 (for 19/289), there are only 50 possible values with denominators of 1,000 with the same four-digit-rounded percentage, and if you round to a five-digit-percentage, this goes down to 5.
Another way of looking at this is, with a maximum denominator of 100 and rounding to four digits, there is only one way to get to 0.2604, which is by dividing 25 by 96.

* Showing the overall relationship between maximum denominator size, degree of rounding/number of given digits, and the proportion of possible numerator/denominator pairs.
This can provide guidance as to how identifiable your data is and to what extent you can mitigate that by rounding percentages.

Caveats: numerators and denominators are both positive integers, numerator is  <= denominator, denominator!=0.
