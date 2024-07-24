#!/usr/bin/python3
import csv

class Student:
    def __init__(self, email, name):
        self.email = email
        self.name = name

    def save_to_csv(self):
        with open('students.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([self.email, self.name])
