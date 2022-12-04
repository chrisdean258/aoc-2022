fn score(s) {
	if s == "A X" 3 + 0
   	else if s == "A Y" 1 + 3
   	else if s == "A Z" 2 + 6
   	else if s == "B X" 1 + 0
   	else if s == "B Y" 2 + 3
   	else if s == "B Z" 3 + 6
   	else if s == "C X" 2 + 0
   	else if s == "C Y" 3 + 3
   	else if s == "C Z" 1 + 6
   	else if s == "A X\n" 3 + 0
   	else if s == "A Y\n" 1 + 3
   	else if s == "A Z\n" 2 + 6
   	else if s == "B X\n" 1 + 0
   	else if s == "B Y\n" 2 + 3
   	else if s == "B Z\n" 3 + 6
   	else if s == "C X\n" 2 + 0
   	else if s == "C Y\n" 3 + 3
   	else if s == "C Z\n" 1 + 6
	else {
		print(s)
		0
	}
}


s = 0
while { a = getline(); a != null } {
	s += score(*a)
}

print(s)
