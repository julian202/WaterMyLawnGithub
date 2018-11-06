# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_python37_render_template]
import datetime
from darksky import forecast
from datetime import date, timedelta
from datetime import datetime as dt
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def root():

	#######################

	BOSTON = 34.277215, -77.836957
	t = dt(2018, 10, 28, 1)
	#t = dt(2018, 11, 4, 1).isoformat()
	day = timedelta(days=1)
	t_minus1 = (t-day).isoformat()
	t_minus2 = (t-2*day).isoformat()
	t_minus3 = (t-3*day).isoformat()
	t_minus4 = (t-4*day).isoformat()
	t = t.isoformat()

	with forecast('8b19ff2840cd837d214d2bfce73426b8', *BOSTON, time=t) as boston:
		a=24*boston.daily.data[0].precipIntensity
	with forecast('8b19ff2840cd837d214d2bfce73426b8', *BOSTON, time=t_minus1) as boston:
		b=24*boston.daily.data[0].precipIntensity
	with forecast('8b19ff2840cd837d214d2bfce73426b8', *BOSTON, time=t_minus2) as boston:
		c=24*boston.daily.data[0].precipIntensity
	with forecast('8b19ff2840cd837d214d2bfce73426b8', *BOSTON, time=t_minus3) as boston:
		d=24*boston.daily.data[0].precipIntensity
	with forecast('8b19ff2840cd837d214d2bfce73426b8', *BOSTON, time=t_minus4) as boston:
		e=24*boston.daily.data[0].precipIntensity
		
	
	#######################
	# For the sake of example, use static information to inflate the template.
	# This will be replaced with real information in later steps.
	dummy_times = [a,
				   b,
				   c,
				   d,
				   e
				   ]

	return render_template('index.html', times=dummy_times)


if __name__ == '__main__':
	# This is used when running locally only. When deploying to Google App
	# Engine, a webserver process such as Gunicorn will serve the app. This
	# can be configured by adding an `entrypoint` to app.yaml.
	# Flask's development server will automatically serve static files in
	# the "static" directory. See:
	# http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
	# App Engine itself will serve those files as configured in app.yaml.
	app.run(host='127.0.0.1', port=8080, debug=True)
# [START gae_python37_render_template]
