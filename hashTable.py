import csv
from datetime import datetime

# Dylan Sherwood
# COS226 
# Hash Table Simulator

# Reads in the csv, encodes it to utf8, sets the first row to the column names
# For loop that appends each row by index, making a list of each column
# Then make a dictionary that sets the column name as a key, the list as a value
def file_read():
    with open('MOCK_DATA.csv', mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        rows = []
        for row in reader:
            clean = {col: (val if val.strip() != "" else None) for col, val in row.items()}
            rows.append(clean)
        return rows

#====================================================
# Time tracking 
#====================================================

def timer_start():
    start_time = datetime.now()
#    print(start_time)
    return start_time

def timer_end(start_time):
    end_time = datetime.now()
    elapsed_time = end_time - start_time
    return elapsed_time


# takes in the rows and the column identifier, sets size to the len of rows
# creates a table by calling table check with the row, column and size
def hash_build(rows, column):
    size = len(rows)
    start_time = timer_start()
    table, collisions = table_check(rows, column, size)
    end_time = timer_end(start_time)
    space = table.count(None)
    return table, end_time, collisions, space


#Creates an empty table, empty collisions, and if the key is not none, calls the insert
# with the table, key and row
def table_check(rows, column, size):
    hash_table = [None] * size
    total_collisions = 0
    for row in rows:
        key = row[column]
        if key is None:
            continue
        total_collisions += insert_linear(hash_table, key, row)
    return hash_table, total_collisions


# Sets size to the length of the has table, index calls the hash function
# To return an index value based on the key
# If it reaches an index that is not None, that is a collision, then resizes
# Index by 1 and continues checking
# Returns collision count
def insert_linear(hash_table, key, row):
    size = len(hash_table)
    index = hash_(key, size)
    collisions = 0

    while hash_table[index] is not None:
        collisions += 1
        index = (index + 1) % size # check next spot
    hash_table[index] = row
    return collisions

def hash_(key, size):
    if key is None:
        return None
    total = 0
    for char in key:
        total = total * 31 + ord(char)
    return total % size



def main():

    rows = file_read()

    title_table, time, title_collisions, space = hash_build(rows, 'movie_title')
    # print(title_table)
    print("title collisions =", title_collisions)
    print("time = ", time)
    print("space = ", space)

    quote_table, time, quote_collisions, space = hash_build(rows, 'quote')
    # print(quote_table)
    print("quote collisions =", quote_collisions)
    print("time = ", time)
    print("space = ", space)



if __name__ == "__main__":
    main()