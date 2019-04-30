from flask import Flask, request, render_template
from recommender import recommendation, return_countries
from project4data import cities, countries

app = Flask(__name__)
app.debug = True

@app.route('/', methods=['GET', 'POST'])
def entry_page():
    return render_template('index.html')

@app.route('/ranking_input/', methods=['GET', 'POST'])
def render_message():

    input_names = ['Walking/Tours', 'Nightlife', 'Tropical', 'Art/Culture', 'Food & Drink', 'History']
    user_inputs_from_html = ['walking_rank', 'nightlife_rank', 'tropical_rank', 'art_rank', 'fandd_rank', 'history_rank']
    check_list = [1,2,3,4,5,6]
    new_list = []
    notonetosix = 'You may only use each ranking once'
    less_than_error = 'Your ranking must be between 1 and 6 inclusive'
    error_message = 'Please fill in the full form'

    for idx, value in enumerate(user_inputs_from_html):
        user_input = request.form[value]
        try:
            if 0 < int(user_input) < 7:
                int_input = int(user_input)
            else:
                return render_template('index.html', message=less_than_error)
        except:
            return render_template('index.html', message=error_message)
        new_list.append(int_input)

    if sorted(new_list) == check_list:
        inputs = dict(zip(input_names, new_list))
    else:
        return render_template('index.html', message=notonetosix)

    target = recommendation(inputs)
    corr_country = return_countries(target)

    if len(target) == 1:
        target1 = f"You should check out ... {target[0]}, {corr_country[0]}!"
        return render_template('index.html', message=target1)
    elif len(target) == 2:
        target2 = f"Why not try ... {target[0]}, {corr_country[0]} or {target[1]}, {corr_country[1]}!"
        return render_template('index.html', message=target2)
    else:
        target3 = f"Either {target[0]}, {corr_country[0]}; {target[1]}, {corr_country[1]} or {target[2]}, {corr_country[2]} should be great for you!"
        return render_template('index.html', message=target3)
        

if __name__ == "__main__":
    app.run()
