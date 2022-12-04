#!/home/chris/bin/copper 

fn max(a, b) if a > b a else b
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

m = -1
s = 0

while { line = getline(); line != null } {
	if *line == "\n" {
		m = max(s, m)
		s = 0
	} else {
		s += parse_int(*line)
	}
}

print(m)
