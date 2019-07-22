def predict(row,weight):
	activation = weight[0]
	for i in range(len(row)-1):
		activation += weight[i+1]*row[i]
	return 1 if activation >= 0.0 else -1

# -1 = banana, 1 = apple
# [circularity, color, class]	
dataset = [[0.1,0.8,-1],
	[0.2,0.9,-1],
	[0.1,0.9,-1],
	[0.15,0.85,-1],
	[0.15,0.7,-1],
	[0.9, 0.3, 1],
	[0.8, 0.25, 1],
	[0.9, 0.1, 1],
	[0.7, 0.1, 1],
	[0.7, 0.15, 1]]
weight = [0.0, 1, -1]

for row in dataset:
	prediction = predict(row, weight)
	print("Expected = %d, Predicted = %d" % (row[-1], prediction))

	