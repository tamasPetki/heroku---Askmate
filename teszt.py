import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']

def get_all_user_story():
    try:
        with open(DATA_FILE_PATH) as csvfile:
            readCSV = csv.DictReader(csvfile, delimiter=';')
            # next(readCSV)
            user_stories = []
            for row in readCSV:
                user_stories.append(row)
    except FileNotFoundError:
        user_stories = []
    return user_stories

def write_csv(export_list):
    with open('newlist.csv', 'w') as story_file:
        writer = csv.DictWriter(story_file, fieldnames=DATA_HEADER, delimiter=';')
        writer.writeheader()
        for row in export_list:
            writer.writerow(row)

def newline():
    new_userstory = {"id":"5", "title": "new_title", "user_story": "append user", "acceptance_criteria":"new ac", "business_value":"50", "estimation": "12", "status":"planning"}
    # user_stories = data_handler.get_all_user_story()
    new_row = []
    # max_id = max(int(i['id']) for i in user_stories)
    new_row.append(("id", new_userstory['id']))
    for key, value in new_userstory.items():
        new_row.append((key, value))
    # max_id = max(int(i['id']) for i in user_stories)
    # new_row.append(str(max_id + 1))
    # for value in new_userstory.values():
    #     new_row.append(value)
    # data_handler.write_csv(user_stories)
    print(dict(new_row))

user_stories = get_all_user_story()
# print(user_stories[0]['title'])
user_stories[2]['id'] = "5"
user_stories[2]['title'] = "NEW title"
user_stories[2]['user_story'] = "NEW user"
user_stories[2]['acceptance_criteria'] = "new ac"
user_stories[2]['business_value'] = "50"
user_stories[2]['estimation'] = "12"
user_stories[2]['status'] = "planning"

# print(user_stories)

# write_csv(user_stories)

newline()