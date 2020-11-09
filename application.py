from flask import Flask, render_template
import data_script

app = Flask('__name__')

@app.route('/')
def index():
	casi_totali = str(data_script.casi_totali())
	deceduti = str(data_script.deceduti())
	guariti = str(data_script.guariti())
	nuovi_casi = str(data_script.nuovi_casi())
	terapia_intensiva = str(data_script.terapia_intensiva())
	isolamento_casa = str(data_script.isolamento_domiciliare())
	ricoverati_con_sintomi = str(data_script.ricoverati_con_sintomi())
	data_giornaliera = str(data_script.data_giornaliera())
	totale_positivi= str(data_script.totale_positivi())
	variazione_positivi= str(data_script.variazione_positivi())
	return render_template("index.html", casi_totali = casi_totali, deceduti = deceduti, guariti= guariti, 
		nuovi_casi = nuovi_casi, terapia_intensiva = terapia_intensiva, isolamento_casa= isolamento_casa,
		ricoverati_con_sintomi = ricoverati_con_sintomi, data_giornaliera= data_giornaliera, 
		totale_positivi= totale_positivi, variazione_positivi = variazione_positivi)

@app.route('/mario')
def mario():
	return lol



if __name__ == '__main__':
	app.run(debug = True)



