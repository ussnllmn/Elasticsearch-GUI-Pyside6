start "elasticsearch-7.15.1" "D:\Work\IR\Assignment IR\elasticsearch-7.15.1\bin\elasticsearch.bat"
start "kibana-7.15.1" "D:\Work\IR\Assignment IR\kibana-7.15.1-windows-x86_64\bin\kibana.bat"
echo Opening elasticsearch and kibana& echo.Waiting for kibana then started dev tools in 60 second.
timeout /t 60
start chrome "http://localhost:5601/app/dev_tools#/console"