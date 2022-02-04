from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "Thems that dies the lucky ones!"

# our index route will handle rendering our form
@app.route('/')
def survey():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def guess():
    print(request.form)
    stacks=[]
    if 'stack1' in request.form:
        stacks.append(request.form['stack1'])
    if 'stack2' in request.form:
        stacks.append(request.form['stack2'])
    if 'stack3' in request.form:
        stacks.append(request.form['stack3'])
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['location'] = request.form['locations']
    session['lang'] = request.form['lang']
    session['program'] = request.form['programOptions']
    session['stacks'] = stacks
    if 'comments' in request.form:
        session['comment'] = request.form['comments']
    print(session)
    return redirect('/result')

@app.route('/result')
def result():
    return render_template('result.html')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.