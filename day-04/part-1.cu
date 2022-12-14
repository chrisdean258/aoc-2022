#!/usr/bin/env copper

s = 0
while (a = getline()) != null {
	l = [0, 0, 0, 0]
	line = *a
	i = 0
	n = 0
	while i < len(line) - 1 {
		if '0' <= line[i] && line[i] <= '9' {
			l[n] *= 10
			l[n] += line[i] - '0'
		} else n++
		i++
	}
	if (l[0] <= l[2] && l[3] <= l[1]) || (l[1] <= l[3] && l[2] <= l[0]) {
		s += 1
	}
}
print(s)
