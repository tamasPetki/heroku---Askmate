from flask import Flask, render_template, request, redirect, url_for

import data_handler

app = Flask(__name__)


@app.route('/')
@app.route('/list')
def route_list():
    user_stories = data_handler.get_all_user_story()
    # data_handler.write_csv(user_stories)
    return render_template('list.html', user_stories=user_stories)


@app.route('/story', methods=['GET', 'POST'])
@app.route('/story/<int:id>', methods=['GET', 'POST'])
def story(id=None):
    if request.method == 'GET':
        user_story = {}
        statuses = data_handler.getstatuses()

        if id is not None:
            user_stories = data_handler.get_all_user_story()
            user_story = user_stories[id-1]

        return render_template('forms.html',
                               story=user_story,
                               title='Add user story' if id is not None else 'Update user story',
                               statuses=statuses)
    if request.method == 'POST':
        if id is not None:
            user_stories = data_handler.get_all_user_story()
            user_stories[id-1]['id'] = id
            user_stories[id-1] = dict(request.form)
            data_handler.write_csv(user_stories)
            return redirect('/')
        if id is None:
            new_userstory = request.form
            user_stories = data_handler.get_all_user_story()
            new_row = []
            max_id = max(int(i['id']) for i in user_stories)
            new_row.append(("id",(max_id+1)))
            for key, value in new_userstory.items():
                new_row.append((key, value))
            user_stories.append(dict(new_row))
            data_handler.write_csv(user_stories)
            return redirect('/')

if __name__ == '__main__':
    app.secret_key = 'superserver_secret'
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )
