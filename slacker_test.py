from slacker import Slacker
token = "xoxp-86428459589-86428459653-86424392214-3cccbe148dfa807dc9d6704ce94b8e73"
slack = Slacker(token)
slack.files.upload('200w.gif',channels = "#api_testing")
