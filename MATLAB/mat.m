% Load your dataset
data = load('your_dataset.mat');
X = data.X; % Input features
y = data.y; % Target variable

% Split the dataset into training and testing sets
train_ratio = 0.8; % 80% for training, 20% for testing
train_size = round(train_ratio * size(X, 1));
X_train = X(1:train_size, :);
y_train = y(1:train_size, :);
X_test = X(train_size+1:end, :);
y_test = y(train_size+1:end, :);

% Train the linear regression model
model = fitlm(X_train, y_train);

% Predict on the test set
y_pred = predict(model, X_test);

% Evaluate the model
mse = mean((y_pred - y_test).^2);
fprintf('Mean Squared Error: %.4f\n', mse);