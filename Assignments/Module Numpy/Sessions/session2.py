
import numpy as np

# 1.Create a NumPy array called my_scores using np.array() with your last 5 Zomato order ratings (pick any integers between 1 and 5), and print the array.

my_scores = np.array([4, 5, 4, 3,5])
print(my_scores)

# 2.Use np.arange() to generate an array of all even numbers between 10 and 30 (inclusive), then print the result.

arr1 = np.arange(10, 30, 2)
print(arr1)

# 3.Generate an array of 8 equally spaced values between 0 and 1 using np.linspace(), and print the array.<br><br><em><strong>Hint:</strong> This is similar to how Spotify creates smooth volume sliders.</em>

arr2 = np.linspace(0, 1, 8)
print(arr2)

# 4.Simulate a Flipkart-style 'Add to Cart' button counter by creating a NumPy array of 10 zeros using np.zeros(), then update the 3rd and 7th items to 1 (representing items added to cart), and print the updated array.

arr3 = np.zeros((10))

arr3[[2,6]] = 1
print(arr3)


# 5.Use np.random.randint() to create an array of 6 random integers between 1000 and 9999 (representing random OTP codes like Paytm), and print the array.<br><br><em><strong>Constraint:</strong> Set the random seed to 42 using np.random.seed(42) before generating the array so your results are reproducible.</em>

np.random.seed(42)
arr4 = np.random.randint(1000, 9999, 6)
print(arr4)







