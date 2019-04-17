from flask import render_template, flash, session, url_for, redirect, request, g, Blueprint, make_response

from . import db
from .auth import login_required

bp = Blueprint('sessions', __name__)

@bp.route('/sessions/add/<int:course_id>')
@login_required
def add_session(course_id):
    con = db.get_db()
    cur = con.cursor() 

    cur.execute("""
        INSERT INTO sessions (course_id, session_name, day, start_time, end_time)
        VALUES (%s, %s, %s, %s, %s)
    """,
    (course_id, 'A', 'M', '12:00:00', "1:00:00"))

    con.commit()

    cur.close()
    con.close()

    return redirect(url_for('courses.edit_courses', id=course_id))
    
