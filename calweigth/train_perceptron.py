def predict(row,weight):
	activation = weight[0]
	for i in range(len(row)-1):
		activation += weight[i+1]*row[i]
	return 1 if activation >= 0.0 else -1
	
def train_weight(train, l_rate, epoch):
	weight = [0.0 for i in range(len(train[0]))]
	for n in range(epoch):
		sum_error = 0.0
		for row in train:
			prediction = predict(row, weight)
			error = row[-1] - prediction
			sum_error = sum_error + error**2
			weight[0] = weight[0] + l_rate*error
			for i in range(len(row)-1):
				weight[i+1] = weight[i+1] + l_rate * error * row[i]
		print ("epoch=%d, lrate=%.3f, error=%.3f" % (n, l_rate, sum_error))
	return weight
	
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
	
l_rate = 0.1
n_epoch = 5
weight = train_weight(dataset, l_rate, n_epoch)
print(weight)