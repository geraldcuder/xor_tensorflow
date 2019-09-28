#! /usr/bin/env python

import numpy as np
from keras.models import Sequential
from keras.layers.core import Dense


def main():
    """
    Trains a neural network on the XOR-Problem and saves the trained weights and the architecture
    to the models/-directory for later use

    """
    # Define model input
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], "float32")
    y = np.array([[0],[1],[1],[0]], "float32")

    # Define model
    model = Sequential()
    model.add(Dense(16, input_dim=2, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))

    # Compile model
    model.compile(loss='binary_crossentropy',
                  optimizer='adam',
                  metrics=['accuracy'])

    # Fit model on data
    model.fit(X, y, epochs=500, verbose=1)

    # Save trained weights and architecture
    model.save("models/model.h5")


if __name__ == "__main__":
    main()
