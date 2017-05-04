# Self Check from
# http://interactivepython.org/runestone/static/pythonds/Introduction/ObjectOrientedProgramminginPythonDefiningClasses.html
# Create a two new gate classes, one called NorGate the other called NandGate.
# NandGates work like AndGates that have a Not attached to the output. NorGates
# work lake OrGates that have a Not attached to the output.

# Create a series of gates that prove the following equality:
# NOT (( A and B) or (C and D)) is that same as NOT( A and B ) and NOT (C and D)
# Make sure to use some of your new gates in the simulation.


class LogicGate:

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
        if super().performGateLogic(self):
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
