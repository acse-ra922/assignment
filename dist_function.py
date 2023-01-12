import timeit
def distance(s,parameters):
    """
    This function takes three arguments: 
    A string 's' consisting of colors of cars separated by the space character
    A string 'parameters' consisting of two colors (A,B) separated by a comma
    
    The function returns the shortest distance between all pairs of cars of 
    colours A and B in the input string.
    
    The function assumes that two lines of input will be provided.
    The first line of the input contains a string of colors
    And the second line of the input contains a pair of colors (A,B)
    
    
    Parameters
    ----------
    
    s: String
      A string of car colors
    
    parameters: String
      Pair of car colors
      
    Returns
    -------
    
    dist: integer
      Minimum distance between pair of car colors
    
    
    Examples
    --------
    
    >>> s = "blue yellow violet red green red"
    >>> parameters = "blue, red"
    >>> print(distance(s,parameters))
    >>> 3
    
    
    >>> s = "blue yellow red"
    >>> parameters = "red, blue"
    >>> print(distance(s,parameters))
    >>> 2
    
    >>> s = "red red blue red"
    >>> parameters = "red, blue"
    >>> print(distance(s,parameters))
    >>> 1
    
    >>> s = "yellow yellow blue yellow yellow red"
    >>> parameters = "red, blue"
    >>> print(distance(s,parameters))
    >>> 3
    
    """
    a,b = parameters.split(", ")
    if a==b:
        return 0
    cars = s.split(" ") #creating a list of the colored cars from the input string
    n = len(cars)         
    dist = n+1          #initializing the variable that will store the minimum distance between two cars
    for i in range(n):
        if cars[i]==a or cars[i]==b:
            prev = i     #variable that marks the position of the occurence of one of the parameters
            break
    while i < n:         #traversing the list of colored cars
        if cars[i] == a or cars[i] == b:
            if cars[prev] != cars[i] and (i - prev) < dist : 
                dist = i - prev      #updating the minimum distance if its greater than the difference                         
                prev = i             #between the two colors passed as arguments
            else:
                prev = i             #updating the value of prev and i variable to continue traversing
        i += 1                       #the list of colors
        
    return dist    

  
def main():
    """
    Main function to accept input and return the distance between two colors
    """
    s = input("Enter a string of colors")
    parameters = input("Enter a pair of colors separated by a comma")
    print(distance(s,parameters))
    
#main()  #uncomment to run the main function  

def time_analysis():
    """
    Time and Complexity Analysis

    This function is to analyze the time and space complexity of the dist_function
    The dist_function has a time complexity of O(n) as it consists of programming statements with
    a complexity of constant time (O(1)) and a for loop and a while loop, both of which have a 
    complexity of O(n).
    """
    timeit.timeit(distance("blue yellow red","blue, red"))