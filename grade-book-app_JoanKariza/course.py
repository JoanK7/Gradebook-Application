#!/usr/bin/python3
import csv

class Course:
    def __init__(self, name, trimester, credits):
        self.name = name
        self.trimester = trimester
        self.credits = credits

    def save_to_csv(self):
        with open('courses.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([self.name, self.trimester, self.credits])

    @staticmethod
    def get_course_credits(course_name):
        with open('courses.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row[0] == course_name:
                    return float(row[2])
        return 0

