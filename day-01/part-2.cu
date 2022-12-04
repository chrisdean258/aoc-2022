#!/home/chris/bin/copper

top3 = [0,0,0]

fn parse_int(str) {
	tot = 0
	i = 0
	while i < len(str) && str[i] >= '0' && str[i] <= '9' {
		tot *= 10
		tot += str[i] - '0';
		i++
	}
	tot
}

fn maybe_insert(l, v) {
	if v > l[0] {
		l[2] = l[1]
		l[1] = l[0]
		l[0] = v
	} else if v > l[1] {
		l[2] = l[1]
		l[1] = v
	} else if v > l[2] {
		l[2] = v
	}
}

s = 0

while { line = getline(); line != null } {
	if *line == "\n" {
		maybe_insert(top3, s)
		s = 0
	} else {
		s += parse_int(*line)
	}
}

print(top3[0] + top3[1] + top3[2])
