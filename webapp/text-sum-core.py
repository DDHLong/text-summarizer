from flask import Flask, render_template, request, send_file
from werkzeug import secure_filename
app = Flask(__name__)

@app.route('/text-summarizer')
def ignite():
   return render_template('main-page.html')

@app.route('/result_text',methods = ['POST', 'GET'])
def result_text():
	if request.method == 'POST':
		result = request.form
		text_tring = result['Text']
		from abberivator_flow import scriptum_abberivator as sa
		out_text_file = open('out.txt', 'w')
		out_text_file.write(sa.summarize(text_tring))
		out_text_file.close()
		return send_file('out.txt', as_attachment=True)
		#return sa.summarize(text_tring)

@app.route('/result_wiki',methods = ['POST', 'GET'])
def result_wiki():
	if request.method == 'POST':
		result = request.form
		text_tring = result['Text']
		from abberivator_flow import wikipedia_abberivator as wa
		out_text_file = open('out.txt', 'w')
		out_text_file.write(wa.summarize(text_tring))
		out_text_file.close()
		return send_file('out.txt', as_attachment=True)
		#return wa.summarize(text_tring)

@app.route('/result_pdff',methods = ['POST', 'GET'])
def result_pdff():
	if request.method == 'POST':
		f = request.files['file']
		f.save(secure_filename(f.filename))
		from abberivator_flow import pdf_abberivator as pa
		out_text_file = open('out.txt', 'w')
		out_text_file.write(pa.summarize(text_tring))
		out_text_file.close()
		return send_file('out.txt', as_attachment=True)
		#return pa.summarize(f.filename)

if __name__ == '__main__':
   app.run(debug = False)