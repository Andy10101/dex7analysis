dex7analysis
============

Python and JavaScript code to manage dexecom7 xml export

1) produce d3 consumable data

run python script first to produce d3 json

PY dependencies: scipy, ipython, lxml, pandas
bash-3.2$ ipython --pylab
%run process.py
#assuming cgm.xml is in current dir
saveD3json(90)

#or pass in path to export.xml
saveD3json(90,"<<path to dexecom export.xml>>")

In same dir run tmp webserver and see results at
bash-3.2$ python -m SimpleHTTPServer 8001
browser: http://localhost:8001/index.html