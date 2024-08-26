import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
(x_train, y_train), (x_test, y_test) = mnist.load_data()
# Normalize pixel values to the range [0, 1]
x_train = x_train.astype('float32') / 255
x_test = x_test.astype('float32') / 255

# Flatten the 28x28 images into 1D vectors
x_train = x_train.reshape(x_train.shape[0], -1)
x_test = x_test.reshape(x_test.shape[0], -1)

# Convert class labels to one-hot encoded vectors
num_classes = 10  # Number of possible digit classes
y_train = tf.keras.utils.to_categorical(y_train, num_classes)
y_test = tf.keras.utils.to_categorical(y_test, num_classes)
model = Sequential()
model.add(Dense(128, activation='relu', input_shape=(784,)))  # Input layer with 784 neurons (28x28 image)
model.add(Dense(128, activation='relu'))  # Hidden layer with 128 neurons
model.add(Dense(num_classes, activation='softmax'))  # Output layer with 10 neurons for 10 digit classes

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(x_train, y_train, epochs=10, batch_size=128, validation_data=(x_test, y_test))
test_loss, test_acc = model.evaluate(x_test, y_test)
print('Test accuracy:', test_acc)
predictions = model.predict(x_test)
predicted_labels = [tf.argmax(prediction, axis=-1) for prediction in predictions]
