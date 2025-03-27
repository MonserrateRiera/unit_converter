from flask import Flask, render_template, request

app = Flask(__name__)

lenght_conversion_factors = {
    'cm': 0.01,
    'm': 1.0,
    'km': 1000.0,
    'inches': 0.0254,
    'yards': 0.9144,
    'miles': 1609.34
}

weight_conversion_factors = {
    'mg': 0.001,
    'g': 1.0,
    'kg': 1000.0,
    'ounce': 28.35,
    'pound': 453.60,
}



def unitConverter (number, unitFrom, unitTo, conversion_factor) -> float:
    #Transform the number in to the standard (meters, grams or celsius)
    number_in_standard = float(number) * conversion_factor[unitFrom]

    #Transform the startard number into the selected unit.
    converted_number = number_in_standard / conversion_factor[unitTo]
    return converted_number




@app.route("/", methods=['GET', 'POST'])
def lenght():

    if request.method == 'GET':
        return render_template('index.html', values = lenght_conversion_factors, unit = "")
    elif request.method =='POST':
        number = request.form['lenghtNumber']
        unitFrom = request.form['unitFrom']
        unitTo = request.form['unitTo']
        
        convertedNumber = unitConverter(number, unitFrom, unitTo, lenght_conversion_factors) 
        return render_template('index.html', result=convertedNumber, number=number, unit_from=unitFrom, unit_to=unitTo, values = lenght_conversion_factors, unit = "")

@app.route("/weight", methods=['GET', 'POST'])
def weight():

    if request.method == 'GET':
        return render_template('index.html', unit="weight", values=weight_conversion_factors)
    elif request.method =='POST':
        number = request.form['lenghtNumber']
        unitFrom = request.form['unitFrom']
        unitTo = request.form['unitTo']
        convertedNumber = unitConverter(number, unitFrom, unitTo, weight_conversion_factors) 
        return render_template('index.html', result=convertedNumber, number=number, unit_from=unitFrom, unit_to=unitTo, unit="weight", values=weight_conversion_factors)
if __name__ == "__main__":
    app.run(debug=True)