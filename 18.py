# 10/30/16
layers = []
for line in open('18.txt').readlines():
	layers.append([int(s) for s in line.split()])

def combine_layers(bottom, top):
	# len(bottom) = len(top) + 1
	# can combine top[i] with bottom[i] or bottom[i + 1]
	next_bottom = [x for x in top]
	for i in range(len(next_bottom)):
		next_bottom[i] += max(bottom[i], bottom[i + 1])
	return next_bottom

def solve():
	current_bottom = layers[-1]
	for i in reversed(range(len(layers) - 1)):
		current_bottom = combine_layers(current_bottom, layers[i])
	[answer] = current_bottom
	return answer

print solve()