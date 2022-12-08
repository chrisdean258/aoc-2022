#!/usr/bin/env copper

fn value(chr) {
	if 'a' <= chr && chr <= 'z' chr - 'a' + 1
	else if 'A' <= chr && chr <= 'Z' chr - 'A' + 1 + 26
	else {
		print("error")
		0
	}
}

s = 0
while (a = getline()) != null {
	line = *a
	mask = 0
	i = 0
	while i < len(line) / 2 {
		mask |= 1 << value(line[i])
	}
	while i < len(line) {
		mask &= ~(1 << value(line[i]))
	}

}
print(s)
