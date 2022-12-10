#!/usr/bin/env copper

fn value(chr) {
	if 'a' <= chr && chr <= 'z' chr - 'a' + 1
	else if 'A' <= chr && chr <= 'Z' chr - 'A' + 1 + 26
	else {
		print("error ", chr)
		0
	}
}

fn bit_idx(mask) {
	i = 0
	while mask > 1 {
		i++
		mask >>= 1
	}
	i
}

s = 0
while (a = getline()) != null {
	line = *a
	mask1 = 0
	mask2 = 0
	i = 0
	while i < len(line) / 2 {
		mask1 |= 1 << value(line[i++])
	}
	while i < len(line) - 1 {
		mask2 |= 1 << value(line[i++])
	}
	s += bit_idx(mask1 & mask2)
}
print(s)
