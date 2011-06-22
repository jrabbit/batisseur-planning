import sys

if __name__ == '__main__':
    if sys.argv[1] == "brecht":
        import parser
        f = open("/var/tmp/distcc.bep")
        x = parser.Parser("/var/tmp/distcc.bep", f)
        print x
    elif sys.argv[1] == "jrabbit":
        import transitional
        x = transitional.Old_Bep("/var/tmp/distcc.bep")
        print x.data
