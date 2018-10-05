import os


def test(q):
    print(q)
    os.system('python stream_psi.py'+" " + str(q))
    result = open("result.txt", "r")
    expected = open("expect.txt", "r")
    r = result.readline()
    s = expected.readline()
    while r:
        if r != s:
            print(r)
            print(s)
            return False
        r = result.readline()
        s = expected.readline()
    return True


if __name__ == "__main__":
    for i in range(1):
        print(test(i))