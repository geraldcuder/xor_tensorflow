#! /usr/bin/env python

from keras.models import load_model
import numpy as np


def main():
    # load model
    try:
        model = load_model('models/model.h5')
    except:
        print('No model found! Please use "make train" to create one!')

    # Start user-input loop
    while True:

        # Get user input
        user_input = input("input> ")

        # Exit the loop
        if user_input == "exit":
            return False

        # Convert it to a numpy-array of the correct shape
        try:
            X_new = np.array(user_input.split(','), dtype='float32').reshape(1, 2)
        except ValueError:
            print('Please enter an integers of shape x, y (i.e. 0,1) !!!')
            continue

        # Check if input is in the correct range
        if (X_new.max() > 1) or (X_new.min() < 0):
            print('Please enter integers that are either 0 or 1 (i.e. 0,1)!')
            continue

        if X_new.shape[1] != 2:
            print('Please enter only two integers at once (i.e. 0,1)!')
            continue

        y_pred = model.predict(X_new).round()

        print('output> ' + str(y_pred.ravel()[0]))


if __name__ == "__main__":
    main()
