# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    assert len(sequence) > 0 and isinstance(sequence,str),"I need a string of a valid length!" 

    permutations = []


    if len(sequence) == 1 :

        return [sequence]


    for variant in get_permutations(sequence[1:]):

        for i in range(len(variant)+1):

            permutations.append(variant[:i]+sequence[0]+variant[i:])


    return permutations




    
if __name__ == '__main__':
   #EXAMPLE
   example_input = 'abcdefg'
   print('Input:', example_input)
   print('Expected Output:', 'I don\'t know')
   print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)
