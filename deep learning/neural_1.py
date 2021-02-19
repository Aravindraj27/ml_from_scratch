# 3-2
# vectors for weights biases and inputs -- vector muliplication or operaitons using lists
# 1 and 2 - 2 weights for each connection and thus 6 - each input should be multiplied twice by weights 
# 3*1 should result in 2*1 after multiplication 
# x1, x2, x3 - input set -- w1 w3 w5 and w2 w4 w6 - weights - b1 b2 biases
# inputs - lists of list each sublist -size 3 and no of sublists no of features
#  no of outputs and no of weight sets are same
x = [[1,2,3],[3,4,5],[2,2,4],[4,5,6]]  #- 4 inputs
w = [[0.2,0.4,0.3],[0.1,1.2,0.3]]
b = 2

def dot_product(vec1, vec2):
    prod = 0
    for i,j in zip(vec1, vec2):
        prod+=i*j
    return prod

def layer(feature, weights, biases):
    output = []
    for weight_set in weights:
        out = dot_product(feature, weight_set) +b 
        output.append(out)
    return output

outputs = []
for feature in x:
    result = layer(feature, w, b)
    outputs.append(result)

for i,j in zip(x, outputs):
    print(f'the output for the features {i} is {j}')
    

