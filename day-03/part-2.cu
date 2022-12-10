#!/usr/bin/env copper-release

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
	line1 = *a
	line2 = *getline()
	line3 = *getline()

	mask1 = 0
	mask2 = 0
	mask3 = 0
	i = -1
	while ++i < len(line1) - 1 {
		mask1 |= 1 << value(line1[i])
	}
	i = -1
	while ++i < len(line2) - 1 {
		mask2 |= 1 << value(line2[i])
	}
	i = -1
	while ++i < len(line3) - 1 {
		mask3 |= 1 << value(line3[i])
	}
	s += bit_idx(mask1 & mask2 & mask3)
}
print(s)
