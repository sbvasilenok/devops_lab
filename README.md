### Install
To install package switch to test environment (optional), goto dist directoy and then run in console:
$ pip install *.whl

### Usage 
To start application simply run in console:
$ svsyslogger

### Config 
You can set output parameters in config.conf which is in `...site-packages/svsyslogger/` directory. You could see the full path to config when app is starting.
For output in json format set option `output=json`
For output in plain text set `output=plain` or remove/comment "output" option.
For change logging interval set "interval" parameter in seconds. If not present, default is 300s.
For change path where logs are saving set "logpath" to appropriate directory. If not present, logfile would be created in `...site-packages/svsyslogger/` directory. You could see the full path to logfile when app is starting.