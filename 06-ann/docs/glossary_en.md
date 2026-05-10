# Assignment Study Glossary - English

This glossary summarizes the key concepts learned in Assignment 6 (artificial neural networks for housing price regression with Keras).

## 1. Artificial Neural Network (ANN)
An ANN is a model made of stacked layers of small computational units (neurons) that learns parameters from data to map inputs to outputs.
Example: A dense network with two hidden ReLU layers learns to map property features to a continuous price.

## 2. Dense (fully connected) layer
A layer where every neuron is connected to every neuron in the previous layer, computing `z = W·x + b` followed by an activation.
Example: `layers.Dense(64, activation="relu")` applies a 64-neuron transformation with ReLU.

## 3. Activation function
A non-linear function applied after the linear part of a neuron. Without it, stacking layers collapses to a single linear transformation.
Example: ReLU (`max(0, x)`) is the default for hidden layers; linear is used for regression outputs.

## 4. ReLU
Rectified Linear Unit. Returns 0 for negatives and the input itself for positives. Cheap and stable in practice for hidden layers.

## 5. Linear output activation
For regression, the output neuron has no activation (or `linear`) so it can produce any real value, matching the unbounded target.

## 6. Loss function
Scalar that measures how wrong the predictions are. The optimizer minimizes it during training.
Example: `mse` for regression, `binary_crossentropy` for binary classification.

## 7. MSE (Mean Squared Error)
Average of squared residuals. Penalizes large errors more than small ones, which is fine when outliers are not extreme.

## 8. MAE (Mean Absolute Error)
Average of absolute residuals. Easier to read because it is in the same units as the target. More robust to outliers than MSE.

## 9. RMSE (Root Mean Squared Error)
Square root of the MSE. Same units as the target and useful as a stakeholder-friendly metric.

## 10. R² (coefficient of determination)
Fraction of the variance in the target explained by the model. R² = 1 is perfect, R² = 0 means the model is no better than predicting the mean.

## 11. Optimizer
Algorithm that updates the weights using the gradient of the loss.
Example: `Adam` adapts per-parameter step sizes; `SGD` with momentum is simpler but more learning-rate sensitive.

## 12. Adam
Adaptive moment estimation. Combines a moving average of gradients and squared gradients, with bias correction. Good default for prototypes.

## 13. SGD with momentum
Plain stochastic gradient descent that keeps a fraction of the previous update direction. Helps cross flat regions and noisy gradients.

## 14. Learning rate
Size of the parameter update at each step. Too large → divergence; too small → slow training and risk of stalling.

## 15. Batch size
Number of training samples used per weight update. Smaller batches add noise (regularizing); larger batches give smoother but less frequent updates.

## 16. Epoch
One full pass over the training set. Models typically need many epochs to converge and benefit from monitoring after each one.

## 17. Backpropagation
Algorithm that computes the gradient of the loss with respect to every weight by applying the chain rule from output back to input.

## 18. Forward pass
The step where the inputs flow through the network to produce predictions. Backprop uses the cached intermediate values.

## 19. Overfitting
The model learns the training data too well, including noise, and generalizes poorly. Spotted as a growing gap between training and validation losses.

## 20. Underfitting
The model is too small or too poorly trained to capture the signal. Both training and validation metrics stay bad.

## 21. Train / validation / test split
Train fits the parameters, validation tunes hyperparameters and decides when to stop, test reports the final unbiased performance. Validation must never leak into the test set.

## 22. K-Fold cross validation
Repeats the train/validation split K times to get a more stable estimate of model performance. Reported as a mean ± std across folds.

## 23. EarlyStopping
Callback that stops training when validation loss stops improving for a number of epochs (`patience`) and restores the best weights.

## 24. Dropout
Randomly disables a fraction of neurons during training. Acts as a regularizer by preventing co-adaptation between units.

## 25. L2 regularization (weight decay)
Adds `λ · ||w||²` to the loss to penalize large weights. Keeps the network simple and reduces overfitting.

## 26. Standardization (z-score)
Rescales each numerical feature to mean 0 and std 1. Should be fitted on training data only and then applied to validation and test.

## 27. One-hot encoding
Represents a categorical variable as a vector of binary indicators. Avoids imposing an artificial order between categories.

## 28. Multicollinearity
High correlation between input features. Can make a linear model unstable. Less harmful for small dense networks but still worth checking.

## 29. Residual
The difference between actual and predicted values. Plotting residuals vs predictions helps detect bias and heteroscedasticity.

## 30. Baseline model
A simple model (here, linear regression) used as a reference point. If a more complex model does not clearly beat the baseline, the extra complexity may not be justified.

## 31. Ensemble (averaging)
Training several models with different seeds and averaging their predictions. Reduces variance at the cost of more compute.

## 32. Model serialization
Saving a trained model to disk in a portable format (`.keras` or `.h5`) so it can be reloaded without retraining.

## 33. Reproducibility
Fixing random seeds (`numpy`, `tensorflow`, `random`) and recording dependencies so that re-running the notebook yields the same numbers.

## 34. Skewness
Asymmetry of a distribution. Right-skewed price targets often have a long tail of expensive properties that drive most of the error.

## 35. Multilayer Perceptron (MLP)
Another name for a feed-forward dense network. The architecture used in this assignment is an MLP with two hidden layers.
