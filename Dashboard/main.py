from flask import Flask, render_template, jsonify
import numpy as np
from scipy.interpolate import griddata

app = Flask(__name__)

# Drei feste Punkte definieren (x, y, z)
FIXED_POINTS = np.array([
    [1, 1, 2],    # Punkt 1
    [4, 2, 5],    # Punkt 2
    [2, 5, 3]     # Punkt 3
])

def interpolate_z(x, y):
    """Interpoliert den z-Wert für einen gegebenen x,y-Punkt"""
    return griddata(
        FIXED_POINTS[:, :2],  # x,y Koordinaten der bekannten Punkte
        FIXED_POINTS[:, 2],   # z-Werte der bekannten Punkte
        np.array([[x, y]]),   # Punkt für den interpoliert werden soll
        method='linear'
    )[0]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get-z/<float:x>/<float:y>')
def get_z(x, y):
    z = interpolate_z(x, y)
    return jsonify({
        'z': float(z),
        'fixed_points': FIXED_POINTS.tolist(),
        'current_point': [x, y, float(z)]
    })

if __name__ == '__main__':
    app.run(debug=True) 