from flask import Blueprint, render_template, url_for, flash, redirect, request, abort

from flask import jsonify

bp=Blueprint('sample', __name__)

@bp.route('/')
def home():
    
    # 
    return ""

@bp.route('/user_request', methods=['GET', 'POST'])
def userRequest():
    
    # Get user request and extract Intent and Entity to query the database and fetch top 5 results
    return ""