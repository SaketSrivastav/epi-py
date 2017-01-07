import sys

class RabinKarp():
    # Prime number to use while generating hash
    prime = 3

    def search(self, t, s):
        """
         Input: t -> text in which we need to search
                s -> search pattern
         Output: True is match found, False if match not found
         Description:
             Compute hash of the pattern and then compute hash of all substring
             of length of pattern in text using rolling hash. When hash matches
             then compare the pattern and substring in case hash returned is
             same as pattern but substring is not.
        Application: Detect plagiarism. No two documents should generate same hash.
        """
        n = len(t)
        m = len(s)
        t_hash = self.create_hash(t, m)
        s_hash = self.create_hash(s, m)
        if self.check_equal(t, s, t_hash, s_hash, 0, m-1):
            return 0
        for i in xrange(1, n-m+1):
            t_hash = self.recalculate_hash(t_hash, ord(t[i]), ord(t[i+m-1]), s)
            if self.check_equal(t, s, t_hash, s_hash, i, i+m-1):
                return i
        return -1

    def check_equal(self, t, s, t_hash, s_hash, s_index, e_index):
        if t_hash != s_hash:
            return False
        if s_index > e_index:
            return False
        for i in xrange(s_index, e_index):
            if s[i - s_index] != t[i]:
                return False
        return True

    def create_hash(self, s, end):
        """
        hash_value = a + bx + cx^2
        """
        hv = 0
        for i in xrange(end):
            hv += (ord(s[i]) * pow(self.prime, i))
        return hv

    def recalculate_hash(self, old_hash, s_value, n_value, pattern):
        """
        new_hash = ((old_hash - a) / x) + cx^2
        """
        nhv = int((old_hash - s_value) / self.prime)
        nhv = int(nhv + (n_value * pow(self.prime, len(pattern)-1)))
        return nhv

def test_substring_search():
    print "###### test_substring_search starts ######"
    rk = RabinKarp()
    s = "acbccabc"
    print "Input: " + s
    p = "abc"
    index = rk.search(list(s), list(p))
    if index == -1:
        print "Error: expected match"
    else:
        print "Output: %s found in %s at %u" % (p, s, index)

    print "###### test_substring_search starts ######"
    s = "aabccabc"
    print "Input: " + s
    p = "abc"
    index = rk.search(list(s), list(p))
    if index == -1:
        print "Error: expected match"
    else:
        print "Output: %s found in %s at %u" % (p, s, index)
    print "###### test_substring_search ends ######"

    print "###### test_substring_search starts ######"
    s = "acbccacc"
    print "Input: " + s
    p = "abc"
    index = rk.search(list(s), list(p))
    if index != -1:
        print "Error: expected match"
    else:
        print "Output: %s not found in %s" % (p, s)
    print "###### test_substring_search ends ######"



def main(argv):
    test_substring_search()

if __name__ == '__main__':
    main(sys.argv)
