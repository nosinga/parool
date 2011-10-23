When memory is running out a reboot does not always work
sudo reboot

better to kill the processes first which eat all the memory (python)

this one worked for me:
ps ax | grep python | grep -v grep | awk '{print $1}' | sudo xargs kill -9

this one seems better, however the top one is easier to read for me

ps ax | awk '/[p]ython/{print $1}' |  sudo xargs kill -9

##  internet comment
## Apart from the fact that there's pkill and killall (depending on the OS), there are quite a lot of things that can be improved in this command line.
## 
## First, this is a nice trick to avoid the ugly "grep -v grep" part:
## ps ax | grep '[p]rocessname'
## 
## Note that the first letter is enclosed in square brackets. This regular expression will match 'processname', but it will not match the grep command itself.
## 
## Second, it doesn't make sense to pipe from grep to awk because awk has a "built-in grep":
## ps ax | awk '/[p]rocessname/{print $1}'

