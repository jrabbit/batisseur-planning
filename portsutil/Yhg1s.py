#Public Domain
#From Yhg1s on #Python
import sys

def file_to_dict(fname):
    d = {}
    current = None
    with open(fname) as f:
        for line in f:
            if not line.lstrip() or line.lstrip().startswith('#'):
                # Comment line, skip.
                continue
            key, sep, value = line.partition('=')
            if sep:
                # Simple KEY="value" line.
                value = value.rstrip()
                # Make sure the value starts and ends with quotes.
                assert value[0] == '"' and value[-1] == '"'
                # Add the value without the quotes.
                d[key] = value[1:-1]
                continue
            key, brace, comment = line.partition("{")
            if brace:
                # Compound 'NAME {' statement, possibly with a comment after
                # it. Read everything until the closing brace on column 0.
                data = [comment]
                for line in f:
                    if line.startswith('}'):
                        break
                    data.append(line)
                d[key] = ''.join(data)
                continue
            print "Warning: unhandled line %r" % line
        return d

def main(argv):
    d = file_to_dict(argv[1])
    print d

if __name__ == '__main__':
    main(sys.argv)