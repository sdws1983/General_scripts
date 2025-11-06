import sys
import os
import numpy as np

np.random.seed(0)

vcf = sys.argv[1]
out = sys.argv[2]
seed = sys.argv[3]

np.random.seed(int(seed))

fout = open(out, 'w')
with open(vcf) as f:
	for i in f:
		o = []
		ii = i[:-1].split("\t")
		for e in range(len(ii)):
			if e <= 3:
				o.append(ii[e])
			else:
				if ii[e] == "9":
					o.append("0")
					o.append("0")
				else:
					t = float(ii[e])/2
					result_list = [t, 1-t]
					p = np.array(result_list)
					index = np.random.choice([1, 2], size=2, p = p.ravel())
					index = [str(x) for x in index]
					o.append(sorted(list(index))[0])
					o.append(sorted(list(index))[1])
					#out += ("\t" + "/".join(sorted(list(index))) + ":" + ":".join(ii[t].split(":")[1:]))
		fout.write(" ".join(o) + "\n")
fout.close()
