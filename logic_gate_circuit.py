# Self Check from
# http://interactivepython.org/runestone/static/pythonds/Introduction/ObjectOrientedProgramminginPythonDefiningClasses.html
# Create a two new gate classes, one called NorGate the other called NandGate.
# NandGates work like AndGates that have a Not attached to the output. NorGates
# work lake OrGates that have a Not attached to the output.

# Create a series of gates that prove the following equality:
# NOT (( A and B) or (C and D)) is that same as NOT( A and B ) and NOT (C and D)
# Make sure to use some of your new gates in the simulation.

#********************************
# http://interactivepython.org/runestone/static/pythonds/Introduction/ProgrammingExercises.html
# Additional Optomizations:

# DONE 1. Research other types of gates that exist (such as NAND, NOR, and XOR). Add
# them to the circuit hierarchy. How much additional coding did you need to do?

# DONE 2. The most simple arithmetic circuit is known as the half-adder. Research the
# simple half-adder circuit. Implement this circuit.\
#   A half-adder takes two inputs (the two binary digits being added) and
#   generates two out puts--the sum and the carry.

# DONE 3. Now extend that circuit and implement an 8 bit full-adder.

# 4. The circuit simulation shown in this chapter works in a backward direction.
# In other words, given a circuit, the output is produced by working back
# through the input values, which in turn cause other outputs to be queried.
# This continues until external input lines are found, at which point the user
# is asked for values. Modify the implementation so that the action is in the
# forward direction; upon receiving inputs the circuit produces an output.


class LogicGate(object):

    def __init__(self, n):
        self.name = n
        self.output = None

    def getName(self):
        return self.name

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output


class BinaryGate(LogicGate):

    def __init__(self, n, A=None, B=None):
        LogicGate.__init__(self, n)

        self.pinA = A
        self.pinB = B

    def getPinA(self, A=None):
        if self.pinA is None:
            return int(input("Enter Pin A input for gate "+self.getName()+"-->"))
        elif type(self.pinA) is not int:
            return self.pinA.getFrom().getOutput()
        return self.pinA

    def getPinB(self, B=None):
        if self.pinB is None:
            return int(input("Enter Pin B input for gate "+self.getName()+"-->"))
        elif type(self.pinB) is not int:
            return self.pinB.getFrom().getOutput()
        return self.pinB

    def setNextPin(self, source):
        if self.pinA is None:
            self.pinA = source
        else:
            if self.pinB is None:
                self.pinB = source
            else:
                print("Cannot Connect: NO EMPTY PINS on this gate")


class AndGate(BinaryGate):

    def __init__(self, n, A=None, B=None):
        BinaryGate.__init__(self, n, A, B)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a == 1 and b == 1:
            return 1
        else:
            return 0


class NAndGate(AndGate):
    """take value or AndGate and NOT it"""
    def __init__(self, n, A=None, B=None):
        AndGate.__init__(self, n, A, B)

    def performGateLogic(self):
        if super(NAndGate, self).performGateLogic():
            return 0
        return 1


class OrGate(BinaryGate):

    def __init__(self, n, A=None, B=None):
        BinaryGate.__init__(self, n, A, B)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a == 1 or b == 1:
            return 1
        else:
            return 0


class NOrGate(OrGate):
    """take value or OrGate and NOT it"""
    def __init__(self, n, A=None, B=None):
        OrGate.__init__(self, n, A, B)

    def performGateLogic(self):
        if OrGate.performGateLogic(self):
            return 0
        return 1


class XOrGate(OrGate):
    """true if either, but not both, are true, false otherwise"""
    def __init__(self, n, A=None, B=None):
        OrGate.__init__(self, n, A, B)

    def performGateLogic(self):
        if self.getPinA() == self.getPinB():
            return 0
        return 1


class XNOrGate(XOrGate):
    """NOT of the exclusive or"""
    def __init__(self, n, A=None, B=None):
        super(XNOrGate, self).__init__(n, A, B)

    def performGateLogic(self):
        """invert the XOr of the inputs"""
        if super(XNOrGate, self).performGateLogic():
            return 0
        return 1


class UnaryGate(LogicGate):

    def __init__(self, n, A=None):
        LogicGate.__init__(self, n, A)

        self.pin = A

    def getPin(self):
        if self.pin is None:
            return int(input("Enter Pin input for gate "+self.getName()+"-->"))
        elif type(self.pinB) is not int:
            return self.pin.getFrom().getOutput()
        return self.pinB

    def setNextPin(self, source):
        if self.pin is None:
            self.pin = source
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")


class NotGate(UnaryGate):

    def __init__(self, n, A=None):
        UnaryGate.__init__(self, n, A)

    def performGateLogic(self):
        if self.getPin():
            return 0
        else:
            return 1


class Connector:

    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate

        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate


def half_adder(A, B):
    """adds two binary numbers

    takes two inputs (the two binary numbers being added) and
    generates two out puts--the sum and the carry.  The two inputs
    can only be one 1 bit (e.g, either 0 or 1)."""

    sum_gate = XOrGate("Sum", A, B)
    carry_gate = AndGate("Carry", A, B)

    return sum_gate.getOutput(), carry_gate.getOutput()


def full_adder(A, B, CIn):
    """The full adder has three inputs - A, B, and the carry - and two outputs -
    the sum and the carry. A and B are 1 bit (0 or 1).

    It can be implemented using two half adder circuits. The first will half
    adder will be used to add A and B to produce a partial Sum. The second half
    adder logic can be used to add CIN to the Sum produced by the first half
    adder to get the final S output. If any of the half adder logic produces a
    carry, there will be an output carry. Thus, COUT will be an OR function of
    the half-adder Carry outputs."""

    partial_Sum = half_adder(A, B)
    CInSum = half_adder(CIn, partial_Sum[0])
    COut = OrGate("COut", partial_Sum[1], CInSum[1])

    return CInSum[0], COut.getOutput()


def full_adder_eight_bit(A, B, CIn=0):
    """a chain of full-adders where the carry out of the previous is the carry
    in of the next

    A and B are 8 bit binary numbers"""

    if type(A) == str:
        A = A[2:]

    if type(B) == str:
        B = B[2:]

    A = str(A)
    B = str(B)
    while len(A) < 8:
        A = "0"+A
    while len(B) < 8:
        B = "0"+B

    one_bit = full_adder(int(A[-1]), int(B[-1]), CIn)
    two_bit = full_adder(int(A[-2]), int(B[-2]), one_bit[1])
    three_bit = full_adder(int(A[-3]), int(B[-3]), two_bit[1])
    four_bit = full_adder(int(str(A)[-4]), int(str(B)[-4]), three_bit[1])

    five_bit = full_adder(int(str(A)[-5]), int(str(B)[-5]), four_bit[1])
    six_bit = full_adder(int(str(A)[-6]), int(str(B)[-6]), five_bit[1])
    seven_bit = full_adder(int(str(A)[-7]), int(str(B)[-7]), six_bit[1])
    eight_bit = full_adder(int(str(A)[-8]), int(str(B)[-8]), seven_bit[1])

    result = str(eight_bit[0])+str(seven_bit[0])+str(six_bit[0])+str(five_bit[0]) + \
        str(four_bit[0]) + str(three_bit[0]) + str(two_bit[0])+str(one_bit[0])

    return result, int(result, 2)


def main():
    """NOT (( A and B) or (C and D)) == NOT( A and B ) and NOT (C and D)"""

    A = int(raw_input("Enter 0 or 1 for A:"))
    B = int(raw_input("Enter 0 or 1 for B:"))
    C = int(raw_input("Enter 0 or 1 for C:"))
    D = int(raw_input("Enter 0 or 1 for D:"))
    # NOT (( A and B) or (C and D))
    g1 = AndGate("G1", A, B)  # for A and B
    g2 = AndGate("G2", C, D)  # for C and D
    g3 = NOrGate("G3")  # NOT((AandB) OR (CandD))

    c1 = Connector(g1, g3)
    c2 = Connector(g2, g3)

    NotABorCD = g3.getOutput()

    # NOT( A and B ) and NOT (C and D)
    n1 = NAndGate("N1", A, B)  # for NOT A and B
    n2 = NAndGate("N2", C, D)  # for NOT C and D
    n3 = AndGate("N3")  # (NOTAandB) and (NOTCandD)

    d1 = Connector(n1, n3)
    d2 = Connector(n2, n3)

    NotABandNotCD = n3.getOutput()

    print "Not((A and B) or (C and D)) =", NotABorCD
    print "Not(A and B) and Not(C and D) =", NotABandNotCD

