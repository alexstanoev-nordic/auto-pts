"""RFCOMM test cases"""

from testcase import TestCase, TestCmd

def test_cases(pts):
    """Returns a list of RFCOMM test cases
    pts -- Instance of PyPTS"""

    test_cases = [
        TestCase("RFCOMM", "TC_RFC_BV_01_C",
                 TestCmd("rctest -n -P 1 %s" % pts.bd_addr(), 20)),

        TestCase("RFCOMM", "TC_RFC_BV_02_C",
                 TestCmd("rctest -r -P 1 %s" % pts.bd_addr())),

        TestCase("RFCOMM", "TC_RFC_BV_03_C",
                 TestCmd("rctest -r -P 1 %s" % pts.bd_addr())),

        TestCase("RFCOMM", "TC_RFC_BV_04_C",
                 TestCmd("rctest -r -P 1 %s" % pts.bd_addr(), stop_wid = 15)),

        TestCase("RFCOMM", "TC_RFC_BV_05_C",
                 TestCmd("rctest -n -P 4 %s" % pts.bd_addr(), 20)),

        TestCase("RFCOMM", "TC_RFC_BV_06_C",
                 TestCmd("rctest -r -P 1 %s" % pts.bd_addr())),

        TestCase("RFCOMM", "TC_RFC_BV_07_C",
                 TestCmd("rctest -r -P 1 %s" % pts.bd_addr(), stop_wid = 14)),

        TestCase("RFCOMM", "TC_RFC_BV_08_C",
                 TestCmd("rctest -r -P 1 %s" % pts.bd_addr())),

        TestCase("RFCOMM", "TC_RFC_BV_11_C",
                 TestCmd("rctest -r -P 1 %s" % pts.bd_addr())),

        TestCase("RFCOMM", "TC_RFC_BV_13_C",
                 TestCmd("rctest -r -P 1 %s" % pts.bd_addr())),

        TestCase("RFCOMM", "TC_RFC_BV_15_C",
                 TestCmd("rctest -r -P 1 %s" % pts.bd_addr())),

        TestCase("RFCOMM", "TC_RFC_BV_17_C",
                 TestCmd("rctest -d -P 1 %s" % pts.bd_addr())),

        TestCase("RFCOMM", "TC_RFC_BV_19_C"),

        # INC PTS issue #13011
        TestCase("RFCOMM", "TC_RFC_BV_21_C"),
        TestCase("RFCOMM", "TC_RFC_BV_22_C"),

        TestCase("RFCOMM", "TC_RFC_BV_25_C",
                 TestCmd("rctest -r -P 1 %s" % pts.bd_addr()))
    ]

    return test_cases

def main():
    """Main."""

    import sys
    sys.path.append("..") # to be able to locate ptscontrol
    import ptscontrol
    pts = ptscontrol.PyPTS()

    test_cases_ = test_cases(pts)

    for test_case in test_cases_:
        print
        print test_case
        for cmd in test_case.cmds:
            print cmd

if __name__ == "__main__":
    main()
