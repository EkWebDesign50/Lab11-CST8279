from flask import Flask, render_template
from modules import convert_to_dict
app = Flask(__name__)

presidents_list = convert_to_dict("presidents.csv")

print(presidents_list[0])