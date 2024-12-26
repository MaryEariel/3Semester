def gen_random(num_count, begin, end):
    p=4765356337; q=39857473; r=408369587
    ans=[]; seed = num_count**begin+end
    while num_count>0:
        seed = (seed*p + q) % r
        ans.append(begin + seed%(end-begin+1))
        num_count-=1
    return ans