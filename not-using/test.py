from canvasapi import Canvas
import json
import requests

ACCESS_TOKEN = "1872~S6SgZc53NpXCnnRGNAEnNCUlXSTFPD5KXBvcaj7UejcCXK5G6i425l6tWjMWsnDR"

BASE_URL = "https://biola.instructure.com"

canvas = Canvas(BASE_URL, ACCESS_TOKEN)
course = canvas.get_course(49885)
enroll = course.get_enrollments()

print(enroll)
