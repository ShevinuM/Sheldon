import torch
import torch.nn as nn

class NeuralNet(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(NeuralNet, self).__init__()
        # Initialize the class with input size, hidden size, and number of classes
        # input_size: Size of the input features
        # hidden_size: Number of neurons in the hidden layers
        # num_classes: Number of classes in the output layer
        
        # Create the first linear layer
        self.l1 = nn.Linear(input_size, hidden_size)
        # l1: Linear layer from input to the first hidden layer
        
        # Create the second linear layer
        self.l2 = nn.Linear(hidden_size, hidden_size)
        # l2: Linear layer from the first hidden layer to the second hidden layer
        
        # Create the third linear layer
        self.l3 = nn.Linear(hidden_size, num_classes)
        # l3: Linear layer from the second hidden layer to the output layer
        
        # Create the ReLU activation function
        self.relu = nn.ReLU()
        # relu: Rectified Linear Unit activation function
    
    def forward(self, x):
        # Forward pass computation through the neural network
        
        out = self.l1(x)
        # Compute the first linear transformation from input to hidden layer
        # x: Input to the network
        # l1: First linear layer
        
        out = self.relu(out)
        # Apply the ReLU activation function to introduce non-linearity
        # relu: Rectified Linear Unit activation function
        
        out = self.l2(out)
        # Compute the second linear transformation from hidden layer to hidden layer
        # l2: Second linear layer
        
        out = self.relu(out)
        # Apply the ReLU activation function again
        
        out = self.l3(out)
        # Compute the final linear transformation from hidden layer to output layer
        # l3: Third linear layer
        
        return out
        # Return the final output of the network