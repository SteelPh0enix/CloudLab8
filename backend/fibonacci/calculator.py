from flask import Blueprint, json, jsonify, request

bp = Blueprint('calculator', __name__, url_prefix='/calculate')

def calculate_fibonacci(value: int) -> int:
    if value <= 0:
        return 0
    if value == 1:
        return 1
    return calculate_fibonacci(value - 1) + calculate_fibonacci(value - 2)

@bp.route('/<int:number>', methods=['GET'])
def calculate(number: int):
    if number < 40:
        value = calculate_fibonacci(number)
        return jsonify(requested=number, value=value, requested_value_too_big=False)
    else:
        return jsonify(requested=number, value=0, requested_value_too_big=True)