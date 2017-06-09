# Write a Python program to insert a new column in existing DataFrame. 

Define a function that takes in the dictionary 'exam_data' and the list 'labels' given below as parameters. The function should convert the 'exam_data' into a DataFrame with the list 'labels' as the index.
Create a new column 'color' with the values given below and return the new DataFrame.

    exam_data  = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
                'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
                'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
                'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
    labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    color = ['Red','Blue','Orange','Red','White','White','Blue','Green','Green','Red']