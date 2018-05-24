"""
Final exam, problem 4.

Authors: David Mutchler, Dave Fisher, Matt Boutell, Amanda Stouder,
         their colleagues and Eric Morse.  May 2018.

"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.


###############################################################################
# DONE: 2.
#   In this problem, you will go through the methods of the  Pig  class
#   that is defined below, one by one, in the order that they appear.
#   For each method:
#      (a) Read the method's doc-string (i.e., specification in double-quotes).
#            If you do not understand WHAT the method is to do,
#            ask your instructor to clarify it.
#      (b) Implement the method.
#      (c) Write at least SOME code  in  main  that tests your code.
#
###############################################################################

def main():
    """ Tests the  Pig  class. """
    # -------------------------------------------------------------------------
    # WRITE CODE HERE AS NEEDED to TEST the code that you write
    #   in the  Pig  class.  At the least, you must:
    #     -- Construct two Pig objects
    #     -- Call each method that you implement below.
    # -------------------------------------------------------------------------
    pig1 = Pig(150)
    pig2 = Pig(100)
    # Tests get_weight method
    print("Expected pig1 weight = 150")
    print("Actual pig1 weight = {}".format(pig1.get_weight()))
    # Tests eat method
    print("expected pig2 weight = 150")
    pig2.eat(50)
    print("Actual pig2 weight = {}".format(pig2.get_weight()))
    # Tests eat for a year method
    pig1.eat_for_a_year()
    print("Expected pig 1 weight = 66945")
    print("Actual pig1 weight = {}".format(pig1.get_weight()))
    # Tests heavier pig method
    print("Expected heavier pig is pig1")
    pig3 = pig1.heavier_pig(pig2)
    if pig3 is pig1:
        print("Actual heavier pig is pig1")
    else:
        print("Actual heavier pig is pig2")
    # Tests new pig method
    pig4 = pig1.new_pig(pig2)
    print("Expected pig4 is pig1 = False")
    print("Actual pig4 is pig1 = {}".format(pig4 is pig1))
    print("Expected pig4 weight is 66945")
    print("Actual pig4 weight is {}".format(pig4.get_weight()))


class Pig(object):
    def __init__(self, weight):
        """
        What comes in:  The Pig's weight (in pounds).
        Side effects: Sets instance variables as needed by the other methods.
        """
        # DONE: Implement and test this method.
        self.weight = weight

    def get_weight(self):
        """ Returns this Pig's weight. """
        # DONE: Implement and test this method.
        return self.weight

    def eat(self, pounds_of_slop):
        """
        Increments this Pig's weight by the given pounds_of_slop.
        """
        # DONE: Implement and test this method.
        self.weight = self.weight + pounds_of_slop

    def eat_for_a_year(self):
        """
        Calls the   eat   method as many times as needed to make this Pig:
          -- eat 1 pound of slop, then
          -- eat 2 pounds of slop, then
          -- eat 3 pounds of slop, the
          -- eat ... [4 pounds, then 5, then 6, then ... ]
          -- eat 364 pounds of slop, then
          -- eat 365 pounds of slop.
        """
        # DONE: Implement and test this method.
        for k in range(365):
            self.eat(k + 1)

    def heavier_pig(self, other_pig):
        """
        Returns either this Pig object or the other given Pig object,
        whichever is heavier.
        """
        # DONE: Implement and test this method.
        if self.get_weight() > other_pig.get_weight():
            return self
        else:
            return other_pig

    def new_pig(self, other_pig):
        """
        Returns a new Pig whose weight is the weight of the heavier
          of this Pig and the other_Pig.
        """
        # DONE: Implement and test this method.
        if self.get_weight() > other_pig.get_weight():
            new_weight = self.get_weight()
        else:
            new_weight = other_pig.get_weight()
        return Pig(new_weight)


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
